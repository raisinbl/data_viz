import streamlit as st

st.markdown(
"""

# Track

- `acousticness` &emsp; number&lt;float&gt; 
A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic.

&gt;=0 &emsp; &lt;=1

- `artists` &emsp; array of strings 
The artists who performed the track. 

- `danceability` &emsp; number&lt;float&gt; 
Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.

&gt;=0 &emsp; &lt;=1

- `duration_ms` &emsp; integer 
The duration of the track in milliseconds.

- `energy` &emsp;  number&lt;float&gt; 
Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.


- `explicit` &emsp;  boolean 
Whether or not the track has explicit lyrics (`true` = yes it does; `false` = no it does not OR unknown).

- `id` &emsp;  string 
The Spotify ID for the track.

- `id_artists` &emsp;  array of strings 
The artists ID who performed the track. 

- `instrumentalness` &emsp; number&lt;float&gt; 
Predicts whether a track contains no vocals. "Ooh" and "aah" sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly "vocal". The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0.

- `key` &emsp;  integer 
The key the track is in. Integers map to pitches using standard Pitch Class notation. E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on. If no key was detected, the value is -1.

&gt;=-1 &emsp; &lt;=11

- `liveness`  &emsp; number&lt;float&gt; 
Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live.

- `loudness` &emsp; number&lt;float&gt; 
Overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typical range between -60 and 0 db.

- `mode` &emsp;  integer 
Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0.

- `name` &emsp;  string 
The name of the track

- `popularity` &emsp;  integer
The popularity of a track is a value between 0 and 100, with 100 being the most popular. The popularity is calculated by algorithm and is based, in the most part, on the total number of plays the track has had and how recent those plays are.


- `release_date` &emsp;  string 
The date the album was first released.

- `speechiness` &emsp;  number&lt;float&gt; 
Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks.

- `tempo` &emsp;  number&lt;float&gt; 
The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration.

- `time_signature` &emsp;  integer 
An estimated time signature. The time signature (meter) is a notational convention to specify how many beats are in each bar (or measure). The time signature ranges from 3 to 7 indicating time signatures of "3/4", to "7/4". 

&gt;=3 &emsp; &lt;=11

- `valence` &emsp;  number&lt;float&gt; 
A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).

&gt;=0 &emsp; &lt;=1
"""
)