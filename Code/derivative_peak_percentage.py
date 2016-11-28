from essentia import *
from essentia.standard import *
from numpy import *

def derivative_peak_percentage(file):   #Input the name of a file
    hopSize = 128
    frameSize = 2048
    sampleRate = 44100
    guessUnvoiced = True

    peaknumber = 0
    length = 0
    peak_percentage = 0

    run_windowing = Windowing(type='hann', zeroPadding=4 * frameSize)  # Hann window with x4 zero padding
    run_spectrum = Spectrum(size=frameSize * 4)
    run_spectral_peaks = SpectralPeaks(minFrequency=1,
                                       maxFrequency=20000,
                                       maxPeaks=100,
                                       sampleRate=sampleRate,
                                       magnitudeThreshold=0,
                                       orderBy="frequency")
    run_pitch_salience_function = PitchSalienceFunction()
    run_pitch_salience_function_peaks = PitchSalienceFunctionPeaks()
    run_pitch_contours = PitchContours(hopSize=hopSize)
    run_pitch_contours_melody = PitchContoursMelody(guessUnvoiced=guessUnvoiced,
                                                    hopSize=hopSize)
    pool = Pool()   # (Note for Doga) -> Creates a pool for each audio whereas in the other algorithm
                    # the pool is created for only one time

    # Load audio and pass it through the equal-loudness filter
    audio = MonoLoader(filename=file)()
    audio = EqualLoudness()(audio)

    # Cut audio into frames and compute for each frame:
    # spectrum -> spectral peaks -> pitch salience function -> pitch salience function peaks
    for frame in FrameGenerator(audio, frameSize=frameSize, hopSize=hopSize):
        frame = run_windowing(frame)
        spectrum = run_spectrum(frame)
        peak_frequencies, peak_magnitudes = run_spectral_peaks(spectrum)

        salience = run_pitch_salience_function(peak_frequencies, peak_magnitudes)
        salience_peaks_bins, salience_peaks_saliences = run_pitch_salience_function_peaks(salience)

        pool.add('allframes_salience_peaks_bins', salience_peaks_bins)
        pool.add('allframes_salience_peaks_saliences', salience_peaks_saliences)

    # Now, as we have gathered the required per-frame data, we can feed it to the contour
    # tracking and melody detection algorithms:
    contours_bins, contours_saliences, contours_start_times, duration = run_pitch_contours(
        pool['allframes_salience_peaks_bins'],
        pool['allframes_salience_peaks_saliences'])
    pitch, confidence = run_pitch_contours_melody(contours_bins,
                                                  contours_saliences,
                                                  contours_start_times,
                                                  duration)
    n_frame = len(pitch)
    dr = derivative(pitch)
    high_derivative_indexes = [index for index, val in enumerate(dr) if val > 100]
    normalized_derivatives = [val for index, val in enumerate(dr)
                              if index not in high_derivative_indexes]
    low_derivative_indexes = [index for index, val in enumerate(normalized_derivatives) if val < -100]
    normalized_derivatives = [val for index, val in enumerate(normalized_derivatives)
                              if index not in low_derivative_indexes]

    peaknumber = float(count_nonzero(normalized_derivatives))
    length = float(len(normalized_derivatives))
    peak_percentage = (peaknumber/length)*100.0

    return peak_percentage




