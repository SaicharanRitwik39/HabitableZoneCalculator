import streamlit as st

def flux(l, semi): 
    return ((1 / semi)**2) * l  # Reciprocal of the Semi-Major axis, squared, then multiplied by the Luminosity in Lsun

# From Kopparapu et al. 2014. Equation 5, Section 3.1, Page 9
def auFromSeff(l, seff):
    return (l / seff)**0.5  # luminosity divided by the Seff, to the power of a half

# From Kopparapu et al. 2014. Equation 4, Section 3.1, Page 9
def Kopparapu2014(SeffSUN, a, b, c, d, tS):
    return SeffSUN + a*tS + b*((tS)**2) + c*((tS)**3) + d*((tS)**4)

# Values from Kopparapu et al. 2014. Table 1, Page 12
def getSeffBoundary(temp, zone):
    tS = temp - 5780  # Temperature delta

    # Recent Venus 1 Me
    if zone in ["recentVenus", "rv"]:
        SeffSUN = 1.766
        a = 2.136*(10**-4)
        b = 2.533*(10**-8)
        c = -1.332*(10**-11)
        d = -3.097*(10**-15)
        return Kopparapu2014(SeffSUN, a, b, c, d, tS)

    # runaway Greenhouse 1 Me
    if zone in ["runawayGreenhouse", "rg"]:
        SeffSUN = 1.107
        a = 1.332*(10**-4)
        b = 1.580*(10**-8)
        c = -8.308*(10**-12)
        d = -1.931*(10**-15)
        return Kopparapu2014(SeffSUN, a, b, c, d, tS)

    # Maximum Greenhouse 1 Me
    if zone in ["maximumGreenhouse", "mg"]:
        SeffSUN = 0.356
        a = 6.171*(10**-5)
        b = 1.689*(10**-9)
        c = -3.198*(10**-12)
        d = -5.575*(10**-16)
        return Kopparapu2014(SeffSUN, a, b, c, d, tS)

    # Early Mars 1 Me
    if zone in ["earlyMars", "em"]:
        SeffSUN = 0.320
        a = 5.547*(10**-5)
        b = 1.526*(10**-9)
        c = -2.874*(10**-12)
        d = -5.011*(10**-16)
        return Kopparapu2014(SeffSUN, a, b, c, d, tS)

def main():
    st.title("Habitable Zone Calculator")

    luminosity = st.number_input("Please enter the star's luminosity (Lsun)", value=1.0, min_value=0.0, step=0.1)
    semimajor = st.number_input("Please enter the object's semi-major axis (AU)", value=1.0, min_value=0.0, step=0.1)
    starTemp = st.number_input("Please enter the star's temperature (K)", value=5780, min_value=0, step=100)
    
    if st.button("Calculate"):
        a = flux(luminosity, semimajor)

        st.write("This object's Seff: " + str(a))

        recentVenus = getSeffBoundary(starTemp, "rv")
        runawayGreenhouse = getSeffBoundary(starTemp, "rg")
        maximumGreenhouse = getSeffBoundary(starTemp, "mg")
        earlyMars = getSeffBoundary(starTemp, "em")

        st.write("**This system's HZ stats:**")
        st.write("### Distances in AU")
        st.write("Recent Venus (1 Me): " + str(auFromSeff(luminosity, recentVenus)))
        st.write("Runaway Greenhouse (1 Me): " + str(auFromSeff(luminosity, runawayGreenhouse)))
        st.write("Maximum Greenhouse (1 Me): " + str(auFromSeff(luminosity, maximumGreenhouse)))
        st.write("Early Mars (1 Me): " + str(auFromSeff(luminosity, earlyMars)))

        st.write("### Stellar Flux (Effective)")
        st.write("Recent Venus (1 Me): " + str(recentVenus))
        st.write("Runaway Greenhouse (1 Me): " + str(runawayGreenhouse))
        st.write("Maximum Greenhouse (1 Me): " + str(maximumGreenhouse))
        st.write("Early Mars (1 Me): " + str(earlyMars))

        st.write(" ")
        if a < earlyMars:
            st.write("This object is NOT in the Habitable Zone (Beyond Early Mars)")
        elif a <= maximumGreenhouse and a >= earlyMars:
            st.write("This object is in the Optimistic Habitable Zone (Between Maximum Greenhouse and Early Mars)")
        elif a <= runawayGreenhouse and a >= maximumGreenhouse:
            st.write("This object is in the Conservative Habitable Zone (Between Runaway Greenhouse and Maximum Greenhouse)")
        elif a <= recentVenus and a >= runawayGreenhouse:
            st.write("This object is in the Optimistic Habitable Zone (Between Recent Venus and Runaway Greenhouse)")

if __name__ == "__main__":
    main()