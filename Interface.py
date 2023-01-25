import streamlit as st
import PROJECT_CODE as pc
import pickle as pk

model = pk.load(open('model.sav', 'rb'))

st.title('Sales prediction')

st.subheader("Here you can predict the global sales for your product")

platform = st.selectbox('Select the Platform: ',
                  ('PSP','SAT','SNES','NES','GEN','PC','GC',
                   'GB','SCD','WiiU','3DS','PS2','PSV','PS','Wii',
                   'DS','PS3','DC','XB','X360','GBA','N64'))
genre = st.selectbox('Select the Genre: ',
                  ('Action','Puzzle','Sports','Platform',
                   'Shooter','Role-Playing','Simulation','Fighting',
                   'Adventure','Racing','Misc','Strategy'))
publisher = st.selectbox('Select the Publisher: ',
                  ('NCSoft','Mastertronic','Rising Star Games','Take-Two Interactive',
                   'Activision','3DO','THQ','Crave Entertainment','SouthPeak Games',
                   'Gotham Games','id Software','Arena Entertainment','Microsoft Game Studios',
                   'Bethesda Softworks','Ubisoft','Havas Interactive','Infogrames',
                   'D3Publisher','Red Orb','MTV Games','Codemasters','GT Interactive',
                   'Black Label Games','Microprose','Eidos Interactive','Red Storm Entertainment',
                   'Mindscape','Majesco Entertainment','Sammy Corporation','Success',
                   'Hudson Soft','Crystal Dynamics','RTL','Accolade','989 Studios',
                   'Banpresto','Square','ASC Games','Nintendo','Agetec','Namco Bandai Games',
                   'LucasArts','Global Star','City Interactive','Virgin Interactive',
                   'ASCII Entertainment','Hasbro Interactive',
                   'RedOctane','Square EA','Electronic Arts','Universal Interactive',
                   'Valve','Tecmo Koei','Pacific Century Cyber Works','Russel','Tomy Corporation',
                   'Fox Interactive','TalonSoft','Deep Silver','Sega',
                   'Sony Computer Entertainment','Westwood Studios','JVC',
                   '505 Games','Konami Digital Entertainment','Disney Interactive Studios',
                   'Midway Games','Empire Interactive','Enix Corporation','Titus',
                   'SCi','GSP','Level 5','Acclaim Entertainment','Ocean','Capcom',
                   'Valve Software','Koch Media','Natsume','Sony Online Entertainment',
                   'CTO SpA','Maxis','Play It','Square Enix','Rage Software',
                   'Warner Bros. Interactive Entertainment','Unknown','Atari','GameBank',
                   'Pinnacle','Video System','Psygnosis','TDK Mediactive','Vivendi Games'))

na_sales = st.number_input("North America sales (in millions)")
e_sales = st.number_input("Europe sales (in millions)")

if st.button('Click to see the predicted sales'):
    result = (float(pc.predict(platform, genre, publisher, na_sales, e_sales, model))*1000000)
    st.write(f"${result:,.3f}")
    