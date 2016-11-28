# vibrato_analysis
Vibrato Dataset,Detection and Parameterization
## Introduction
This dataset was created as an outcome of a summer internship with Good-sounds project. Sound recordings were used for vibrato analysis. The dataset contains monophonic recordings of single notes and melodies for four instruments with annotations of four different recording sets regarding some vibrato parameters. 

It is organized according to the owner of the recordings. Sounds with vibrato and no vibrato are presented within the folders with their annotations in cvs format. All annotations except than the alto saxophone recordings include derivative analysis of pitch parameters. 

One of the recordings for violin was made in the Universitat Pompeu Fabra recording studio by a violist from MTG. Single notes of two octaves and four different melodies starting from different pitch are recorded in wav format sampled at 44.1 kHz. Each sound separated by semitones is recorded four times for no vibrato,slow, standard and fast rates of vibrato. Melodies  were played for no vibrato and vibrato at a standard rate to have the attenuation at the end of the note. 

One other recording set was taken from Good-sounds project. The only brass instrument within the whole dataset is this one for alto saxophone. It was again recorded in the Universitat Pompeu Fabra / Phonos recording studio. This dataset for alto saxophone not only contains vibrato and non vibrato sounds but also some different tonal characteristics. 

Three other recordings are downloaded from a user named [http://www.freesound.org/people/Carlos_Vaquero/](Carlos_Vaquero). Violin, violoncello and transverse flute recordings were downloaded and used for non commercial purposes under creative commons license. Within the Carlos_Vaquero folder, audio files are separated according to the type of instruments.

## Dataset Description
The database is meant for organizing the sounds in a handy way. It is organized according to the creator. Each has 11 field descriptor. 

  - Carlos_Vaquero
      * Transverse_flute
Violin
Violoncello
Good-sounds-Alto sax
Alto-sax
MTG - Violin
Violin

Except than alto-sax recordings, each contains following parameters:

Peak_Percentage: Percent wise proportion of peaks in first derivation of the pitch trajectory.
Mean_Difference: Mean value of the differences of two consecutive peaks.
Max_Difference: Maximum separation of side by side peaks. 
Index_Max (first one): Index value of the maximum peak in the derivative array
Location_Max (%): Location of the maximum peak in the array, percent wise.
Start_End_Time (seconds): Starting and ending time instants of vibrato in the recording.
Duration: Duration of the vibrato part of the recording.
