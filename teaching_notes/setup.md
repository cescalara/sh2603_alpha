# The Laboratory setup

## Before the lab
1. Get the triple alpha source from the safe
2. Check that the equipment is set up correctly
   * vacuum pump is on
   * power supply is on
   * the LIN AMP OUT is connect to the TUKAN MCA
   * the TUKAN MCA is connected to the LAB computer
   * the lab computer has the TUKAN software installed and running
3. Place the alpha source in the small chamber under the detector, close the door and open the vacuum valve to the chamber
5. Open the vacuum valve to the pump to reach maximum vacuum, then close to avoid air flooding the pump
   * pressure gauge runs from 0 to 1 bar but scale is inverted
4. Turn on the bias voltage of the alpha king spectrometer
5. Run an acquisition with the TUKAN software to check

## Part 1: The range of alpha particles in air
1. Start with discussion of alpha decay and tunneling probability
2. Explain the lab setup including the two Si detectors and the triple source (244-Cm, 241-Am, 239-Pu)
3. Explain the need for calibration and data acquisition using the TUKAN software
4. Using nuclear tables (or IAEA app) find the expected energy of emitted alpha particles
   * 244-Cm: 5805 keV
   * 241-Am: 5485 keV
   * 239-Pu: 5157 keV
5. In order to calibrate the setup run an acquisition up to at least 1000 events
   * It is necessary to use this as a measure, not exposure time, as when air is introduced into the chamber, acquisition will be slowed significantly.
6. Once calibrated, ask what we should expect once air is intriduced gradually into the chamber
   * Energy decrease -> the alpha particles undergo interactions
   * Peak broadening -> due to the stochastic nature of these interactions
7. Students should the use this setup to vary the pressure and record energy values
8. Plotting E vs. P and fitting gives the P values for which E = 0, i.e. the range of the alpha particle is the distance between the source and the detector, which can be measured (P_0 and x_0 are known)
9. Students can use the Ideal Gas Law to find a relation between P and x, which can be used to calculated the range at atmospheric pressure
10. Using this relation students can make a plot of E vs. x, and estimate the stopping power, -dE/dx
    * The final plot of -dE/dx vs. x_mean should show the Bragg peak, accompanied by an explanation
11. Release all vacuum from the chamber and remove the triple alpha source, which should be returned to the safe
12. Turn off the bias voltage on the alpha king spectrometer and close the vacuum valve to the chamber

## Part 2: The unknown source
1. Switch the output cable to the GAUSS LIMIT output of the preamplifier
2. Switch on the bias voltage to 1 kV, setting the gain to 50
3. Open the vauum valve to the larger chamber
4. Place the source holder halfway in with the marker on the right
5. Take an acquisition, 5 peaks should be seen
6. Give the energy of the peaks to the students to allow them to recalibrate (now using different detector)
   * 226-Ra: 4784 keV
   * 210-Po: 5304 keV
   * 222-Rn: 5489 keV
   * 218-Po: 6002 keV
   * 214-Po: 7687 keV
7. Discuss naturally occuring decay chains (see the lab instructions)
8. Using the given energies, students should identify the decaying nuclides and thus the decay chain
9. Discuss qualitatively what can be inferred regarding the age of the source
   * relative height of peaks
   * half-life of different decays

## Part 3: Alpha decay and spontaneous fission
1. Move the source holder to halfway in with the marker on the bottom left
2. Discuss the decay of 252-Cf, which has a small branching ratio for spontaneous fission (3.09%)
3. Change the gain to 5
4. Run a long acquisition (~ 10 min) in order to see small spontaneous fission bumps in the spectrum
5. Use the spectrum to calculate the branching ratio
   * BR_sf = (counts_sf/2) / ( (counts_sf/2) + counts_a )
   * discuss sources of uncertainty and calculation of the measurement error

## Summary
1. Reminder of the key concepts
2. Lab report explanation
3. Switch off all equipment, return alpha source to safe and lock the lab