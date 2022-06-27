import streamlit as st

st.markdown(
    """
# Artist

- `popularity` &emsp;  integer 
The popularity of the artist. The value will be between 0 and 100, with 100 being the most popular. The artist's popularity is calculated from the popularity of all the artist's tracks.

- `id` &emsp;  string 
The Spotify ID for the artist.

- `name` &emsp;  string 
The name of the artist.

- `followers` &emsp;  integer 
The total number of followers.

- `genres` &emsp;  array of strings 
A list of the genres the artist is associated with. If not yet classified, the array is empty.
    """
)