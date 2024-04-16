import asyncio
import traceback
from database_manager import add_test, add_question



async def add_specific_test_questions():
    # Определяем название и отдел только для интересующего нас теста
    name = "CES 6 GMDSS"
    department = "deck"

    try:
        test_id = await add_test(name, department)


        await add_question(test_id,
                           "In a distress-situation a MF/HF-DSC transmission is used in the 8MHz frequency. In this case always: \n\n1) Indicate on what frequency communication will be continued \n\n2) Put in the MMSI number of the coastguard on the DSC \n\n3) Ask the RCC for the frequency \n\n4) Turn on the right frequency",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The person charged with radio distress traffic must be referred to in: \n\n1) The manual \n\n2) The ship's radio log book \n\n3) MERSAR book \n\n4) Safety certificate",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "What are the NAVTEX messages categories which cannot be suppressed? \n\n1) Satnav messages \n\n2) A, B, C \n\n3) A, B, D \n\n4) Weather forecasts",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Which word will precede a safety message? \n\n1) PAN PAN \n\n2) SAFETY \n\n3) URGENT \n\n4) SECURITE",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Satellite communication is usually provided by: \n\n1) Ground wave \n\n2) Sky wave \n\n3) Space wave \n\n4) none of the mentioned",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Messages sent via INMARSAT C are charged: \n\n1) On the number of kilobits of information transmitted per block of 256 bits \n\n2) On the number of kilobits of information transmitted per block of 1024 bits \n\n3) On the basis of a three minute minimum charge with one minute incremental steps \n\n4) On the basis of a six second minimum charge with six second incremental steps",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "You want to send a DSC-call in connection with a shore telephone-call. You must choose: \n\n1) Urgency \n\n2) Distress \n\n3) Routine \n\n4) Safety",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "A distress alert has accidentally been sent with the Inmarsat-C installation. One should now: \n\n1) Call the manager \n\n2) Turn off the transmitter \n\n3) Wait until an RCC reports \n\n4) Make contact with an RCC",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "VHF channel 15 is: \n\n1) Inter-ship channel \n\n2) Distress channel \n\n3) Contra-ship channel \n\n4) Public traffic channel",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "How many maintenance methods must be provided by ships sailing in area A1 and A2 \n\n1) 3 \n\n2) 1 \n\n3) 2 \n\n4) 4",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "The battery of a SART: \n\n1) Must be re-charged weekly \n\n2) Replaced monthly \n\n3) Must be replaced before the expiry date is exceeded \n\n4) Charged condition must be checked weekly",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "The MID is: \n\n1) An INMARSAT mobile number \n\n2) A number which indicates in which area the ship can operate \n\n3) A ship accounting code \n\n4) A number which indicates the nationality of the ship",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "On a MF/HF-transmitter-receiver there is a volume control. Another name for this is: \n\n1) LF-gain \n\n2) RC-gain \n\n3) HF-gain \n\n4) Sensitivity",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "What does the abbreviation VHF mean? \n\n1) Visual High Frequency \n\n2) Very High Frequency \n\n3) Variable High Frequency \n\n4) Variable Hertz Frequency",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "When a character in the NAVTEX message sent is not received in the proper way: \n\n1) Any other character will be printed \n\n2) A closely resembling character will be printed \n\n3) Nothing or a special character will be printed \n\n4) the message will not be printed at all until, with repeated transmission, it can be automatically compared and corrected",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "A satellite receives the transmissions of the 406 MHz Cospas-Sarsat EPIRB. The transmissions of the EPIRB will be: \n\n1) Always passed on to a LUT \n\n2) Exclusively passed on to a LUT if the satellite sees both the EPIRB and the LUT \n\n3) Exclusively passed on to a LUT only between 70 degrees N and 70 degrees S \n\n4) Passed when the satellite in passing the equator",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "What is the first function of GMDSS? \n\n1) Transmission and reception of signals for locating \n\n2) Transmission and reception of on scene communication \n\n3) Reception of shore to ship distress alerts \n\n4) Transmission of ship to shore alerts",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "A distress-call, onboard via RCC, may only be given Receipt if: \n\n1) The O.O.W deems it necessary \n\n2) The captain orders \n\n3) The manager orders \n\n4) OSC from the RCC concerned invites the vessels",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "What statement is correct with frequency modulation? \n\n1) The amplitude remain constant \n\n2) Frequency modulation is often applied in the maritime VHF-range (band) \n\n3) The frequency is constant \n\n4) The amplitude fluctuating an LF-rhythm",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "The word SATCOM is spelled conform the international phonetic alphabet: \n\n1) Sierra, Able, Tripoli, Charlie, Oscar, Mike \n\n2) Sierra, Anna, Tango, Cornelies, Oslo, Mike \n\n3) Sierra, Alfa, Tango, Charlie, Oscar, Mike \n\n4) Sierra, Able, Tango, Cornelies, Oslo, Man",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "MUF stands for: \n\n1) Highest possible frequency that can be made with an HF-transmitter on board \n\n2) Most utilised frequency \n\n3) Most effective frequency, to make a connection with an HF-transmitter \n\n4) Highest possible frequency that will be reflected by the ionosphere",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "When may a call for radio medical advice be preceded by the urgency-signal: \n\n1) In urgent cases \n\n2) When you have a doctor on board \n\n3) Always \n\n4) Never",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Dish aerials are used with: \n\n1) None of the mentioned \n\n2) Inmarsat - B and -M \n\n3) Inmarsat -A and -C \n\n4) Inmarsat -C and -M",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "You receive a distress alert on HF Radio. What should you do? \n\n1) No response is necessary providing the vessel is more than 24 hours away. \n\n2) Relay the message immediately on 2182 kHz. \n\n3) Wait three minutes and if no acknowledgement is heard from a coast station you should relay the alert. \n\n4) Acknowledge receipt.",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Which of the following is a INMARSAT C Mobile Earth Station Identification Number (IMN)? \n\n1) 322753810 \n\n2) 122700 \n\n3) 227530000 \n\n4) 422753810",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "The typical \"daylight-frequencies\" for long distance transmission are located in the: \n\n1) 16 or 22 MHz-band \n\n2) 8 or 12 MHz-band \n\n3) VHF-band \n\n4) 4 or 6 MHz-band",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Which equipment will detect a signal from a SART transponder? \n\n1) Radio Direction Finder \n\n2) X band radar \n\n3) DSC receiver \n\n4) S band radar",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "The word RADIO is spelled conform the international phonetic alphabet: \n\n1) Romeo, Atlanta, Delta, India, October \n\n2) Radio, Alfa, Delta, India, Oscar \n\n3) Romeo, Alfa, Delta, India, Oscar \n\n4) Romeo, Alpha, Delta, India, October",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "The names and addresses of accounting authorities can be found in: \n\n1) The ITU List of Ship Stations \n\n2) The ITU List of Callsigns and Numerical Identities of Stations used by the Maritime Mobile and Maritime Mobile-Satellite Services \n\n3) The ITU List of Radiodetermination and Special Services \n\n4) The ITU List of Coast Stations",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "On area A2 the function 'Transmission of ship to shore distress alerts' is mainly based on: \n\n1) The use of INMARSAT Epirbs \n\n2) The use of SARSAT COSPAS Epirbs \n\n3) The use of VHF DSC \n\n4) The use of MF DSC",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "According to the rules of GMDSS vessels one must be able to receive MSI with the aid of: \n\n1) NAVTEX and EGC-receiver \n\n2) HF and VHF DSC-encoder \n\n3) EPIRB and SART \n\n4) Emergency portable radio",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Which of the following is a ship MMSI? \n\n1) 1227000 \n\n2) 227530000 \n\n3) 2275300 \n\n4) 22753000",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "What is the acronym FR 01? \n\n1) MMSI \n\n2) Call sign \n\n3) AAIC \n\n4) MSI",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "'Fading' can partially be compensated by: \n\n1) Dimmer \n\n2) Clarifier \n\n3) Pre-selector tuning \n\n4) Automatic gain control",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "By FleetNET communication is understood: \n\n1) An EGC-message destined for ships with the same group call number \n\n2) An urgent message for all ships in a particular area \n\n3) A HF-NBDP -message destined for ships in a certain geographical area \n\n4) A MSI-message destined for ships in specific geographical area",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The transmitting range of an HF transmitter is mainly determined by: \n\n1) The height of the transmitting antenna \n\n2) The time of the day in relation to propagation \n\n3) The transmitting power \n\n4) The length of the transmitting antenna",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "The recommended connection between antenna and VHF is: \n\n1) Band cable \n\n2) Electric cable \n\n3) Coaxial cable \n\n4) Three vein cable",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "By the degree of selectivity of a receiver is meant: \n\n1) Ability to prevent variations in the strength of radio frequency signal received\n\n2) Ability to distinguish weak stations from adjacent stronger stations \n\n3) Ability to receive all signals \n\n4) Ability to make weak stations audible ",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "The receipt of a distress alert is to be pronounced as followed: \n\n1) Mayday (1x), call-sign of ship in distress (3x) / this is / own call-sign (3x) / received mayday \n\n2) Mayday (1x) / distress alert / own ship call sign \n\n3) Mayday (3x) / this is / own call-sign (1x) / received mayday / call-sign of ship in distress (1x) \n\n4) Mayday (1x) / this is / own call-sign (3x) / received mayday",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Which of the following watches must a vessel maintain when sailing in Sea Area A1? \n\n1) A continuous DSC watch on 8414.5 Khz plus one other HF DSC frequency \n\n2) A continuous DSC watch on Channel 70 \n\n3) A continuous DSC watch on Channel 16. \n\n4) A continuous DSC watch on 2187.5 kHz.",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "During duplex mode you are able to: \n\n1) Not to interrupt \n\n2) Interrupt after releasing the PTT-switch \n\n3) Interrupt \n\n4) Talk to two stations simultaneously",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Public correspondance VHF communications should normally be operated: \n\n1) In J3E mode – on duplex basis \n\n2) In J3E mode – on simplex basis \n\n3) In G3E mode – on simplex basis \n\n4) In G3E mode – on duplex basis",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "How often must inspection of proper working of the EPIRB's and SART's take place on board? Once per: \n\n1) 14 days \n\n2) Month \n\n3) Week \n\n4) Every day",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "To get priority with radio-communication, one must notify the coast-station that the call is: \n\n1) A priority call \n\n2) A collect call \n\n3) An urgent call \n\n4) A personal call",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "A frequency of 150 MHz has a wavelength of: \n\n1) 200m \n\n2) 2000m \n\n3) 20m \n\n4) 2m",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "When a message is sent by the Inmarsat-C installation to an Internet e-mail address, the land charge is: \n\n1) Independent of the destination \n\n2) Dependent on the destination \n\n3) Dependent on the 'chargeband' \n\n4) Dependent on the type of terminal used",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Which of the following is an Accounting Authority Identification Code? \n\n1) 2187.5 \n\n2) FR01 \n\n3) 227990850 \n\n4) F1B",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "The compulsory testing of a prescribed EPIRB is to be done: \n\n1) Once a week \n\n2) Once a year \n\n3) Once a month \n\n4) Once in 4 years",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "What is the proper term used to describe a coast radio station that primarily handles chargeable ship-to-shore message traffic of a routine nature? \n\n1) Mobile Radio Service. \n\n2) Accounting authority. \n\n3) Network Coordination Station. \n\n4) Public Correspondence Station.",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "The Satellite orbit in the Cospas-Sarsat system is: \n\n1) Polar \n\n2) Geostationary \n\n3) Semi-geostationary \n\n4) helio-synchronous",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Which of the following two digits codes is used to obtain medical advice? \n\n1) 38 \n\n2) 32 \n\n3) 26 \n\n4) 42",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "A DSC-message of the 'safety' category is received from another vessel on VHF channel 70. Conforming to the GMDSS rules, for the continuation of the safety traffic, you must change to VHF-channel: \n\n1) 07 \n\n2) 85 \n\n3) 16 \n\n4) 70",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "To prevent overload of the MF/HF transmitter; \n\n1) Do not transmit too long at full power \n\n2) Switch over to low power intermittently \n\n3) Do not leave the transmitter on stand-by for too long, if not required \n\n4) Clean the dust filter of the fan regularly",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "A SART is used by a vessel in distress. This SART is seen on the screen of a: \n\n1) 3 Cm radar \n\n2) 10 Cm radar \n\n3) Both 3 Cm and 10 Cm radar \n\n4) Special radar",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "A Cospas-Sarsat EPIRB can be used in: \n\n1) Only in the sea-areas A2 and A3 \n\n2) All sea-areas (A1 to A4) \n\n3) Only in sea-area A4 \n\n4) Only in the sea-areas A1, A2 and A3",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "A vessel is equipped for all sea areas. In the middle of the Indian Ocean the EGC-receiver appears out of order. Is it still possible to receive MSI-messages? \n\n1) Yes with VHF DSC \n\n2) NO \n\n3) Yes, with the MF/HF-radio telex \n\n4) Yes, with the MF/HF-DSC",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "You have an important navigational or meteorological warning to transmit. What call should proceed this message when made on the radio telephone? \n\n1) Pan Pan (3 times) \n\n2) Mayday Mayday (3 times) \n\n3) Victor Victor (3 times) \n\n4) Securite Securite (3 times)",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Vessels communicating directly with each other by VHF, work: \n\n1) Always simplex \n\n2) Always duplex \n\n3) Always semi-duplex \n\n4) Dependent on the set on board, either simplex or duplex",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The time indication 121310z means in maritime radio communication: \n\n1) 12th day, 1310 hours local time \n\n2) 12th day, 1310 hours UTC \n\n3) 12th month, 13th day, 1000 hours UTC \n\n4) 12th month, 13th day, 1000 hour Local time",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "In Which publication will you find the working frequencies of coast stations? \n\n1) The ITU List of Ship Stations  \n\n2) The ITU List of Call signs and Numerical Identities of Stations used by the maritime mobile and maritime mobile-satellite services \n\n3) The ITU List of coast stations \n\n4) The ITU List of Radiodetermination and Special Services",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Which of the following regions lies outside Sea Areas A1, A2, and A3? \n\n1) There are no additional Sea Areas. \n\n2) Sea Areas only apply to INMARSAT footprint areas \n\n3) Sea Area A3-I (INMARSAT coverage) and Sea Area A3-S (HF SITOR coverage). \n\n4) Sea Area A4",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "MF communication is usually provided by: \n\n1) Ground wave \n\n2) None of the mentioned \n\n3) Sky wave \n\n4) Space wave",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "On the radio telephony 2182 kHz frequency when are the 'silence periods'? \n\n1) For 6 minutes starting at quarter past and 45 minutes past. \n\n2) For 3 minutes starting on the hour and half hour. \n\n3) For 3 minutes starting at quarter past and 45 minutes past. \n\n4) For 6 minutes starting on the hour and half hour.",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Acoustic feedback can arise: \n\n1) Because the speaker is kept in an open area \n\n2) Because outside noise is amplified by the loudspeaker in the microphone \n\n3) Because the volume adjustment of the speaker is too high \n\n4) Because the loudspeaker works as a microphone",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "The sensitivity of a communication receiver can be adjusted with: \n\n1) Clarifier \n\n2) AF-Gain \n\n3) Squelch \n\n4) RF-Gain",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Which type of call will be sent by a ship sighting another ship in distress which is not itself in position to transmit a distress alert? \n\n1) Distress relay call \n\n2) Distress call \n\n3) Safety call \n\n4) Urgent call",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "What is the travelling speed of radioelectric waves? \n\n1) 9800 km/h \n\n2) The speed of light  \n\n3) The speed of sound \n\n4) 1670 Km/h",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "The wavelength of a radio-signal reflected against the F-layer may be: \n\n1) 15 cm \n\n2) 1.5 m \n\n3) 15 m \n\n4) 150 m",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "The MERSAR is: \n\n1) A survey of vessels favorably located for possible rescue during SAR operations \n\n2) A book for communication regulations at sea \n\n3) A fully automated system for mutual assistance and rescue of persons at sea \n\n4) A book of directions for search and rescue at sea",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "A coast radio station for sea area A2 has at least the following frequencies at its disposal \n\n1) 2187.5 KHz and 2182 KHz \n\n2) 2174 KHz \n\n3) 2187.5 KHz \n\n4) 2187.5, 2182 and 2174.5 KHz",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Which International Convention introduced the GMDSS? \n\n1) MERSAR \n\n2) SOLAS \n\n3) GMDSS \n\n4) STCW",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "On board they want to make a DSC-call with a foreign coast-station. It is an urgent call. Preferably choose: \n\n1) The international DSC-call frequency \n\n2) The international DSC-distress frequencies \n\n3) The national DSC-call frequencies of the coast-station concerned \n\n4) The international DSC-urgent frequency",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Which class of emission is used for VHF DSC transmissions? \n\n1) J3E \n\n2) G3E \n\n3) J2B \n\n4) G2B",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "On board they want to send a safety-call to other vessels. The DSC safety-call: \n\n1) Has to contain a work-frequency \n\n2) May contain a work-frequency \n\n3) May not contain a work-frequency \n\n4) Will automatically send the correct working frequency",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "What transmission-mode must be used with NBDP? \n\n1) E mail \n\n2) J2B / F1B \n\n3) J3E \n\n4) G3E",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "The wave length is: \n\n1) Independent of the frequency \n\n2) Equal to the frequency \n\n3) Inversely proportional to the frequency \n\n4) Proportional to the frequency",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Which of the following is the correct minimum carriage requirement for a ship of more than 300 gross tons and operating in area A1: \n\n1)  1 VHF RT + DSC + DSC watch receiver - 1 or 2 SART - 1 NAVTEX or 1 EGC receiver- 2 or 3 VHF portable\n\n2) VHF RT - 1 or 2 SART - 1 NAVTEX or 1 EGC receiver- 2 or 3 VHF portable \n\n3) 1 MF RT + DSC + DSC watch receiver - 1 or 2 SART - 1 NAVTEX or 1 EGC receiver- 2 or 3 VHF portable - 1 EPIRB \n\n4) VHF RT + DSC + DSC watch receiver - 1 or 2 SART - 1 NAVTEX or 1 EGC receiver- 2 or 3 VHF portable - 1 EPIRB",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "The safety message announces that a station: \n\n1) Will relay a message concerning an important navigational or meteorological warning \n\n2) Is in serious and imminent danger and needs immediate assistance \n\n3) Is going to be under repairs \n\n4) Has an very urgent message concerning the safety of a vessel, a plane or another means of conveyance",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "A MF/HF-DSC multi-frequency call attempt may: \n\n1) Not be repeated \n\n2) Be repeated after 3.5 to 4.5 minutes \n\n3) Be repeated after 15 minutes \n\n4) Be repeated after 1 to 1.5 minutes",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "For a DSC-connection (no 'distress alert') with another vessel the following frequencies are used: \n\n1) TX: 2187.5 kHz RX: 2187.5 kHz \n\n2) TX: 2189.5 kHz RX: 2189.5 kHz \n\n3) TX: 2177.0 kHz RX: 2177.0 kHz \n\n4) Tx: 2187.5 kHz RX: 2182.0 kHz",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "At present the MF/HF transmitter often has an automatic aerial turning unit. Should this fail: \n\n1) You can transmit but cannot receive \n\n2) The transmitter will automatically keep operating on the MF and HF distress frequencies \n\n3) No distress frequencies can be used at all \n\n4) It's always possible to put the turning unit in a fixed position, so the MF distress frequencies can still be used",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "When sending an OBS (weather report) with Inmarsat one should use Service Code '41'. With this address the weather report will always be transmitted to: \n\n1) The meteorological station connected with the CES used \n\n2) KNMI in Holland \n\n3) The meteorological office of the ship's flag state \n\n4) MET office Washington, this office will take care of further dispatch of the weather reports",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "You wish to carry out a test transmission on your radio equipment. What precautions should be taken if any? \n\n1) Listen out to ensure that no safety/distress traffic is in progress. \n\n2) All of the items in the other alternatives should be done. \n\n3) Test transmission should be carried out on artificial aerials and/or reduced power. \n\n4) Test transmission should be kept to a minimum",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "The usual range of a VHF radio-set from ship to ship at sea is: \n\n1) 10 Nautical Miles \n\n2) 2 Nautical Miles \n\n3) 20 Nautical Miles \n\n4) 200 Nautical Miles",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Operator connected R/T calls are charged: \n\n1) On the basis of a six second minimum charge with one second incremental steps \n\n2) On the basis of a six second minimum charge with six second incremental steps \n\n3) On the basis of a one minute minimum charge with one minute incremental steps \n\n4) On the basis of a three minute minimum charge with one minute incremental steps",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "The hydrostatic release of an EPIRB should be changed: \n\n1) Every two years \n\n2) Yearly \n\n3) Every four years \n\n4) Every three years",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The whip-antenna of the MF transceiver was lost in bad weather. The MF-transceiver can be used again: \n\n1) If the whip-antenna is replaced by a Sat C antenna \n\n2) If the whip-antenna is replaced by an antenna of about the same length as the original one \n\n3) If instead of the whip-antenna, another whip-antenna such as the spare VHF antenna is connected \n\n4) Only if the whip antenna is replaced by another whip-antenna of the same length",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "The word NAVTEX is spelled conform the international phonetic alphabet: \n\n1) November, Anna, Victor, Tango, Eduard, X-ray \n\n2) November, Able, Valencia, Tripoli, Echo, Xantippe \n\n3) November, Alfa, Victor, Tango, Echo, X-ray \n\n4) November, Apple, Victoria, Tango, Echo, X-mas",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Radio signals in the HF channels propagate mainly: \n\n1) In a straight line \n\n2) Between the earth and satellites \n\n3) Along the curvature of the earth \n\n4) Through hops between the ionised layers and the earth",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Which action do you perform when you log in to a satellite ocean region? \n\n1) You inform the NCS that the SES is available for communications. \n\n2) You adjust the antenna. \n\n3) You update the ship's position \n\n4) You select the CES through which you wish to send a message.",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Which type of call will be sent by a ship sighting containers adrift in vicinity of her position? (No message about this problem was previously transmitted via NAVTEX or INMARSAT C SAFETYNET) \n\n1) Distress call \n\n2) Safety call \n\n3) Urgent call \n\n4) Distress relay call",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Where should the VHF survival craft transceivers be located during normal operation of the ship? \n\n1) Near the liferaft \n\n2) In the lifeboats \n\n3) On the bridge \n\n4) Near the gangway",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "If on low-power, VHF channels 15 and 17 may be used for: \n\n1) Intership radio traffic \n\n2) Coastal traffic \n\n3) Commercial radio traffic \n\n4) On board communication (inter-ship traffic)",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "What mode is used for broadcast an MF/HF-DSC message: \n\n1) J2B / F1B \n\n2) J3E \n\n3) G3E \n\n4) H3E",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Which word will precede an urgency message? \n\n1) PAN \n\n2) PAN PAN \n\n3) URGENCY \n\n4) MAYDAY",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "What is SELFEC: \n\n1) A one-sided transmission meant for all vessels \n\n2) A Navtex-transmission \n\n3) A one-sided transmission meant for one vessel \n\n4) A facsimile transmission",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "One wishes to have a telephone conversation with a person whose name is known. This is what is called: \n\n1) A call to a known person \n\n2) A collect call \n\n3) A direct call \n\n4) A personal call",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "On which frequencies do most satellite EPIRBs operate? \n\n1) 121.5/406MHz \n\n2) 500Khz \n\n3) 121.5Khz \n\n4) 2182Khz",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Which class of emission is used for HF radio telephony transmissions? \n\n1) F1B \n\n2) J3E \n\n3) G2B \n\n4) G3E",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "What does the abbreviation DSC means? \n\n1) Digital Safety Call \n\n2) Distress and safety call \n\n3) Digital Selective Call \n\n4) Distress Selective Call",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "With what system is a NAVTEX-message transmitted? \n\n1) JRC \n\n2) SELFEC \n\n3) ARQ \n\n4) FEC",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "At sea there is a container adrift which can be a danger for navigation. The call starts with: \n\n1) SECURITE (3x) \n\n2) URGENT (3x) \n\n3) PAN PAN (3x) \n\n4) MAYDAY (3x)",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The word SHIP is spelled conform the international phonetic alphabet: \n\n1) Sierra, Hotel, Item, Papa \n\n2) Sierra, Hotel, India, Papa \n\n3) Singapore, Hotel, India, Paris \n\n4) Sugar, Hotel, Italia, Peter",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "What is the most important factor influencing the VHF range? \n\n1) The type of message sent. \n\n2) The channel used \n\n3) The height of the antenna \n\n4) The size of the antenna",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Which VHF channel should be used for intership navigation safety communications? \n\n1) Ch.12 \n\n2) Ch.16 \n\n3) Ch.06 \n\n4) Ch.13",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "On which frequency must a ship maintain a continuous watch when sailing in area A2? \n\n1) 2187.5 kHz \n\n2) 8414.5 kHz \n\n3) 2182 kHz \n\n4) 4207.5 kHz",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "By wavelength is understood: \n\n1) The propagation speed of a radio vibration in free space \n\n2) The distance travelled by a radio vibration in a period \n\n3) The propagation direction of a radio vibration \n\n4) The length of a single spike in a wave",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Command of radio-traffic between vessels and coast-stations lies: \n\n1) With the station that calls \n\n2) With the station called \n\n3) Always with the coast station \n\n4) With coast guard",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "In the Inmarsat Maritime Communications Handbook one can find information about: \n\n1) Ship's Inmarsat Id's \n\n2) Numbers of fax subscribers \n\n3) Radio telex commands \n\n4) 2 digit code telex services",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "In maritime communication two international treaties are primarily involved. They are: \n\n1) The IMO at London and the ITU at Geneva \n\n2) The Solas and its rules \n\n3) Solas and the international treaty for messaging \n\n4) Gmdss hand book and Mersar",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Which of the following frequency bands would most likely provide reliable communications between two stations that are 15 miles apart? \n\n1) The Medium Frequency (MF) band. \n\n2) The Very High Frequency (VHF) band \n\n3) The High Frequency (HF) band. \n\n4) The Low Frequency (LF) band",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "In what HF-band is long distance transmission possible when both stations are located in Darkness: \n\n1) 4 MHz \n\n2) 16 MHz \n\n3) 8 MHz \n\n4) 22 MHz",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "The MMSI is: \n\n1) An INMARSAT mobile number \n\n2) A ship accounting code \n\n3) A vessel position reporting system \n\n4) A ship identity number",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "When a coastguard-station wants to send a gale-warning by DSC it will happen in the category: \n\n1) Safety \n\n2) Routine \n\n3) Security \n\n4) Urgency",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The log-in of an Inmarsat-C installation is important: \n\n1) To inform the addressee, that one is available for messages offered \n\n2) To inform the NCS that one is available for messages offered \n\n3) To keep watch on Sat-C for safety messages \n\n4) To inform the LES, that one is available for messages offered",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "On board an accident happened. Urgent radio-medical advice is needed. We choose the category: \n\n1) Routine \n\n2) Safety \n\n3) Urgency \n\n4) Distress",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "MMSI is short form of: \n\n1) Merchant Mariners Signal Identity \n\n2) Merchant Marine Ship identity \n\n3) Mobile Maritime Safety Information \n\n4) Maritime Mobile Service Identity",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "What is the purpose of the “SQUELCH” on a VHF transmitter/receiver? \n\n1) Reduce the 'noise' in the background \n\n2) Increase the range of the transmitter \n\n3) Increase the sound signal of the receiver \n\n4) Switch to another channel",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The authority to order the use of distress signal or distress alerts is: \n\n1) Company safety officer \n\n2) Only with the master \n\n3) The first person to discover the distress situation \n\n4) The person designated to maintain communication during distress situations",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "MF radio signals propagate mainly: \n\n1) Between the earth and satellites \n\n2) Through hops between ionised layers and the earth \n\n3) Along the curvature of the earth \n\n4) In a straight line",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Of the AM-signal: \n\n1) Amplitude and frequency of the carrier wave are constant \n\n2) Both amplitude and frequency of the carrier wave are variable \n\n3) Is not dependent on the frequency and amplitude \n\n4) Amplitude is variable and frequency of the carrier wave is constant",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Which one of the listed items has to be included in a distress message? \n\n1) Identification of the ship. \n\n2) Weather in immediate vicinity. \n\n3) Destination. \n\n4) Last port of call.",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "What are the GMDSS sea areas? \n\n1) Near coastal, National and International \n\n2) A1,A2,A3 and A4 \n\n3) Atlantic East, Atlantic West, Indian and Pacific areas \n\n4) AA,AB,AC and AD",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "By the term 'Stand by' the operator of a coast-station means that one should: \n\n1) Wait on this channel for one hour \n\n2) Switch back to the calling channel \n\n3) Wait until the coast-station calls again \n\n4) Give the position of the ship",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "What is the most important factor influencing the HF range? \n\n1) The size of the antenna \n\n2) The channel used \n\n3) The power of the transmitter \n\n4) The frequency used",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "One of the sailors needs urgent medical assistance. The VHF-call starts with: \n\n1) PAN PAN (3x) \n\n2) Urgent (3x) \n\n3) MAYDAY (3x) \n\n4) SOS (3x)",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "DSC uses for automatic identification the MMSI. The identification 002442000 is assigned to: \n\n1) A vessel \n\n2) A coast-station or coast guard-station \n\n3) A type of vessel's \n\n4) A group of vessels",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "What is the purpose of the radiotelephony two tone alarm? \n\n1) Alert COSPAS/SARSAT satellites \n\n2) Attract the attention of the person on watch. \n\n3) Activate bridge watchkeeping receivers and attract the attention of the person on watch. \n\n4) Activate bridge watchkeeping receivers.",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "The following information must be given on the SART: \n\n1) The name of the operator \n\n2) The date of replacement of the hydrostatic release unit \n\n3) The MMSI number sent \n\n4) Date of replacement of the batteries",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "A proper working of the 406 MHz Cospas-Sarsat EPIRB can be tested with: \n\n1) The testing function of the device \n\n2) Regulation monthly test transmissions from RCC's \n\n3) Test transmissions from Cospas-Sarsat satellites \n\n4) Requesting RCC for the test",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The portable walkie talkies required to be carried by GMDSS regulations should have which channels as a minimum? \n\n1) Channels 13 & 16 \n\n2) Channels 6, 13 & 16 \n\n3) Channel 16 only \n\n4) Channels 6 & 16",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "The transmitting receiving method, when both stations can transmit and receive at the same time is called: \n\n1) None of the mentioned \n\n2) Semi-duplex \n\n3) Duplex \n\n4) Simplex",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Your vessel is acting as the on scene commander during a distress rescue. Various vessels are interfering the distress traffic on the VHF. What message would you use to stop them interfering with this traffic? \n\n1) Seelonce pan \n\n2) Seelonce securite \n\n3) Seelonce distress \n\n4) Seelonce mayday",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "The ID of an Inmarsat M station on board starts with: \n\n1) 6 \n\n2) 4 \n\n3) 1 \n\n4) 3",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The proper operation of an Inmarsat C-terminal can be tested by: \n\n1) Requesting a \"self test\" \n\n2) Doing a \"link test\" \n\n3) Sending a message to MF DSC \n\n4) Doing a \"recommissioning test\"",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "According to the rules of GMDSS vessels are equipped with certain radio-communication devices depending on: \n\n1) Flag state \n\n2) Type of vessel \n\n3) The trading sea areas \n\n4) Their tonnage",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Which word will precede a routine message? \n\n1) MAYDAY \n\n2) PAN PAN \n\n3) ROUTINE \n\n4) No specific word will precede a routine message",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "The capacity of a battery is expressed in: \n\n1) ampere x hours \n\n2) Watt x hours \n\n3) volt x hours \n\n4) volt x ampere",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The ideal aerial length depends on: \n\n1) The modulation form chosen \n\n2) The frequency chosen \n\n3) The weather conditions \n\n4) The class of transmission",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "A distress alert from an Inmarsat-EPIRB, is received in the coverage area of a satellite by ground station within: \n\n1) 24 hrs \n\n2) 30 to 60 minutes \n\n3) Two minutes \n\n4) 60 to 90 minutes",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "A distress call has been sent accidentally on your MF DSC equipment. Which of the following is correct for cancelling the false distress alert? \n\n1) Send an all stations urgent priority MF DSC call \n\n4) Switch off the transmitter \n\n2) Send a selective distress priority MF DSC call to the nearest MRCC— Inform it that a false distress alert has been transmitted \n\n3) Make broadcast on 2182 kHz \"Mayday all stations...\" and cancel the false distress alert.",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "The traffic list of a coast-station is a list of: \n\n1) Call-signs of ships for which a radio-telephone call, a telegram or another call is intended \n\n2) Names of ships which, on behalf of safety at sea, are being routed by a traffic control system \n\n3) Name of ship's scheduled for berthing \n\n4) Pertinent navigational -and weather information",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "In daytime, as a result of sunlight, the number of layers of ionisation will: \n\n1) Decrease \n\n2) Increase \n\n3) Keep fluctuating \n\n4) Not change",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "At sea red rocket signals are seen. This is not reported by radio. You have to begin the distress alert procedure via VHF with the term: \n\n1) MAYDAY  \n\n2) MAYDAY RECU \n\n3) MAYDAY RELAY\n\n4) Distress alert",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "The responsibility for the transmitting equipment lies with the: \n\n1) User of the installation \n\n2) Shipping company (owner) \n\n3) Duty officer \n\n4) Master",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "What is the action that a GMDSS Radio Operator should take when a DSC distress alert is received? \n\n1) The Operator should immediately set continuous watch on the radiotelephone frequency that is associated with frequency band on which the distress alert was received. \n\n2) The Operator should immediately set continuous watch on VHF channel 70. \n\n3) The Operator should immediately set continuous watch on the NBDP frequency that is associated with frequency band on which the distress alert was received. \n\n4) No action is necessary, as the DSC control will automatically switch to the NBDP follow-on communications frequency.",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "On board you have to switch from transmitting to receiving and vice versa. The shore station can transmit and receive simultaneously. You are working with two different frequencies. This method is called: \n\n1) Simplex \n\n2) Semi-duplex \n\n3) Semi-simplex \n\n4) Duplex",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Define the class of emission F3E: \n\n1) Radiotelex and DSC - Frequency shift keying of sub-carrier with error correction \n\n2) Single side band suppressed carrier \n\n3) Radiotelephony - Frequency modulation \n\n4) Radiotelephony - Single sideband full carrier",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "What is the meaning of the abbreviation \"RQ\" at the end of a DSC sequence? \n\n1) Problem of transmission \n\n2) Acknowledgment broadcast \n\n3) End of sequence \n\n4) Acknowledgement request",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "At what minimum height above sea level must a SART transponder be mounted? \n\n1) 1 metre \n\n2) 0.5 metre \n\n3) 2 metres \n\n4) The proper function of a SART transponder doesn't depend on the height above sea level",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "On area A1 the function \"Transmission and reception of signals for locating\" is mainly based on: \n\n1) the use of VHF DSC \n\n2) the use of SART transponders \n\n3) the use of INMARSAT Epirbs \n\n4) the use of SARSAT COSPAS Epirbs",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "A received DSC 'distress alert' contains the following information: 'UNDESIGNATED DISTRESS' Of this distress case: \n\n1) Number of person at risk is unknown \n\n2) Time is unknown \n\n3) The nature of distress is unknown \n\n4) The position is unknown",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "You have received the nine digit MMSI of a ship on your DSC equipment. In which publication will you find the name of the ship? \n\n1) The ITU List of Ship Stations \n\n2) The ITU List of Coast Stations \n\n3) The ITU List of Radiodetermination and Special Services \n\n4) The ITU List of Callsigns and Numerical Identities of Stations used by the Maritime Mobile and Maritime Mobile-Satellite Services",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "What is the main purpose of a radio transmitting installation onboard: \n\n1) To enhance the safety of lives at sea \n\n2) Public traffic \n\n3) To talk to friends \n\n4) Safe navigation and internal communication",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "In radio telephony what is the 'URGENCY CALL' which should be used to indicate that you have a very urgent message to transmit concerning the safety of another vessel or person? \n\n1) Securite Securite (3 times) \n\n2) Pan Pan (3 times) \n\n3) Mayday Mayday (3 times) \n\n4) Victor Victor (3 times)",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "VHF communication is usually provided by: \n\n1) Sky wave \n\n2) None of the mentioned \n\n3) Ground wave \n\n4) Space wave",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "With maintenance of batteries it is of primary importance that: \n\n1) There is proper relative humidity in the space where the batteries are stored \n\n2) The space is not oily \n\n3) There is an absolute free access to the battery space \n\n4) The space where the batteries are stored is properly ventilated",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "The signal of an Inmarsat EPIRB: \n\n1) Will immediately be detected within the coverage-area by the satellite's concerned \n\n2) Will be detected within 1 1/2 hours by a passing satellite \n\n3) Can only be detected when a LUT within the range of the satellite \n\n4) Will be detected immediately by the coast station",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The presence of a VHF-installation is primarily intended to: \n\n1) Take part in public traffic \n\n2) Enhance the safety of lives at sea \n\n3) Take part in harbour traffic \n\n4) Take part in intra ship communication",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Which of the following services is not provided by INMARSAT C: \n\n1) Telex \n\n2) Safetynet \n\n3) Telephone \n\n4) Fleetnet",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "The word CHANNEL is spelled conform the international phonetic alphabet: \n\n1) Cornelies, Hotel, Alfa, November, November, Echo, Lima \n\n2) Cornelies, Hotel, Apple, November, November, Echo, Land \n\n3) Charlie, Hotel, Able, November, November, Echo, Liverpool \n\n4) Charlie, Hotel, Alfa, November, November, Echo, Lima",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "The prescribed test of EPIRB, SART and portable VHF radio set must be entered in: \n\n1) Ship's radio log \n\n2) Radio equipment manual \n\n3) Equipment survey \n\n4) Maintenance manual",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The MF/HF-transceiver on board is tuned to the assigned frequency of a station. To make this connection the following mode is used: \n\n1) G3E \n\n2) J3E \n\n3) H3E \n\n4) J2B",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Which of the following is a coast station MMSI? \n\n1) 227530000 \n\n2) 227005300 \n\n3) 2275300 \n\n4) 22753000",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "One can check the functioning of the SART by: \n\n1) Removing it from the holder and turning the SART upside down \n\n2) Activating it by extracting the antenna \n\n3) Lowering SART in to the sea \n\n4) Activating the SART and checking the effect on the radar screen",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Which of the following frequencies is used by the NAVTEX system? \n\n1) 518 Khz \n\n2) 156,8 MHz \n\n3) 121,5 MHz \n\n4) 2182 Khz",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The display of a radiotelephone-installation shows the following selections: Transmitting mode: H3E Transmitting frequency: 2187,5 kHz The transmitting mode indicator is 'flashing'. This can mean that: \n\n1) The radiotelephone-alarm signal must be transmitted now \n\n2) The transmitting mode is not compatible with the chosen frequency \n\n3) The 'H3E' mode is to be selected before transmitting on the 2187,5 kHz band \n\n4) You are ready to press the send button",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "What is understood by carrier frequency: \n\n1) The frequency of upper side band (USB) \n\n2) Frequency of the carrier wave \n\n3) The frequency actually used by transmitter and receiver \n\n4) Frequency of single side band",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "An EPIRB has been activated accidentally. Which of the following is correct for cancelling the false distress alert? \n\n1) Call a LUT and inform it \n\n2) Send a distress priority VHF DSC call and make broadcast to all stations \n\n3) Make broadcast to all stations on VHF 16 \n\n4) Call the nearest coast station and inform it that a false distress alert has been transmitted",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "What is the emergency frequency on M.F. (Medium frequency) radio? \n\n1) 2182 Hz \n\n2) 2617 Hz \n\n3) 1616 Hz \n\n4) 1718 Hz",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The type-indication of the radio set is mentioned in: \n\n1) Registry certificate \n\n2) The safety certificate \n\n3) The equipment appendix \n\n4) The survey of equipment",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Define the class of emission J3E: \n\n1) Radiotelephony - Phase modulation \n\n2) Radiotelex and DSC - Phase modulation \n\n3) Radiotelephony - Single sideband suppressed carrier \n\n4) Radiotelephony - Single sideband full carrier",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "The impedance of a coax cable for the VHF-set depends on: \n\n1) The temperature of the cable \n\n2) The way in which the feed line is controlled \n\n3) The length of the coax cable \n\n4) The structure dimensions and the material of the coax cable",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "For calling a coast-station by VHF one should preferably use: \n\n1) A working channel of the nearest shore-station of that coast-station \n\n2) Channel 70 \n\n3) Channel 16 \n\n4) A special calling channel of that coast-station",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The position that is determined by built in GPS-receiver in an Inmarsat-EPIRB has an accuracy of about: \n\n1) 2200 meters\n\n2) 200 meters  \n\n3) 1200 meters \n\n4) 4200 meters",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "The position of a 406 MHz Cospas-Sarsat EPIRB is: \n\n1) Determined by satellites by means of directional aerials \n\n2) Passed on by the EPIRB to the satellite \n\n3) Measured by the 'dopler' shift in the signals \n\n4) Transmitted by the ship",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Fleetnet communication via the Inmarsat-system is an EGC among other things intended for all: \n\n1) Vessels \n\n2) Vessels coordinating in the rescue operations \n\n3) Vessels in a certain geographical area \n\n4) Vessels of a certain shipping-company",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Which class of emission is used for ARQ NBDP transmissions? \n\n1) F1B \n\n2) G3E \n\n3) G2B \n\n4) J3E",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "A radio-wave travels in the air at a speed of: \n\n1) 300.000 Metres per second\n\n2) 300.000 Kilometers per second  \n\n3) 30.000 Kilometers per hour \n\n4) 300.000 Kilometers per hour",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "A wire antenna of 12 metres in length is probably: \n\n1) An Inmarsat-antenna \n\n2) A VHF-antenna \n\n3) A MF/HF-antenna \n\n4) A Sat-C antenna",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "What is SITREP an abbreviation for? \n\n1) Ship Indication Transmission Equipment. \n\n2) Ship Transit Emergency Radio. \n\n3) Survivor Indication Transponder Equipment. \n\n4) Situation Report.",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Each ship fitted with a radiotelephone station shall listen on the distress frequency during navigation, for how many hours a day according to the regulations? \n\n1) 24 hours \n\n2) 12 hours \n\n3) 16 hours \n\n4) 8 hours",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Which type of call will be sent by a ship adrift and needing the assistance of a tug? (The weather is not bad and the ship will be aground 24 hours later) \n\n1) Safety call \n\n2) Urgent call \n\n3) Distress call \n\n4) Distress relay call",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "The variation in strength of the received signal is called: \n\n1) Selectivity \n\n2) Oscillation \n\n3) Fading \n\n4) Sensitivity",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Pledge of secrecy applies: \n\n1) Only for those who want to send and/or receive a message \n\n2) For everybody \n\n3) For 2nd officer only \n\n4) Only to certificate holders",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "What mode must be used on the MF/HF transmission when making a radiotelephone call: \n\n1) J3E \n\n2) H3E \n\n3) G3E \n\n4) F1B/J2B",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Under GMDSS rules the trading area A3 can be considered to be: \n\n1) Polar region. \n\n2) Within coverage of the INMARSAT system. \n\n3) Within VHF range. \n\n4) Within MF range.",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Satellites which receive the 406 MHz Cospas-Sarsat EPIRB are: \n\n1) Only capable to determine the position of the EPIRB in certain circumstances \n\n2) Not capable to determine the position of the EPIRB \n\n3) Capable to determine the position of the EPIRB \n\n4) Capable to determine position only in day time",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "A personal call means that: \n\n1) The applicant on board request the coastal station to bring about a conversation with a shore subscriber by means of a scrambler \n\n2) The applicant on board request the coast-station to personally guard the conversation with the shore subscriber \n\n3) The applicant wants the call to be charged to some other person \n\n4) The applicant on board wishes to have a conversation with a person whose name is known",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "The emergency battery of a GMDSS portophone: \n\n1) Must be replaced before the expiry date is exceeded \n\n2) Must be charged after expiry date \n\n3) Cannot be replaced \n\n4) Must be tested once a week",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The call sign of a vessel is meant to: \n\n1) Gain a quicker transit at bridges and locks \n\n2) Give others the possibility to identify the vessel \n\n3) To use short name in transmissions to reduce cost \n\n4) Provide the certificate holder with unique identification",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "A MMSI number consist of: \n\n1) 10 digits\n\n2) The call sign followed by 4 digits \n\n3) 9 digits  \n\n4) 6 digits",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Sea area A3 is in maritime radio traffic a sea area: \n\n1) From about 200 miles from shore a reliable DSC connection exists with one or more coastal stations \n\n2) Where communication is not possible \n\n3) With the exception of the sea areas A1 and A2, in which a reliable HF connections exist by DSC with one or more coast radio stations \n\n4) With the exception of the areas A1 and A2 within the range of a geostationary satellite of Inmarsat in which an uninterrupted alerting is possible",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "What do you do after receiving a VHF DSC DISTRESS call? \n\n1) You set watch on VHF channel 16 \n\n2) You send immediately a DSC DISTRESS RELAY call \n\n3) You send immediately a DSC DISTRESS ACKNOWLEDGEMENT call \n\n4) You set watch on channel 13",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Inmarsat is short for: \n\n1) International Maritime Safety Organisation \n\n2) International Maritime Satellite Organisation \n\n3) International Maritime Satellite System \n\n4) Internal Marine Safety Organisation",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Which class of emission is used for VHF radio telephony transmissions? \n\n1) H3E \n\n2) J2B \n\n3) G3E \n\n4) G2B",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Which of the following are exclusively intership RT channels: \n\n1) Channels 05, 06, and 13 \n\n2) Channels 11 and 74 \n\n3) Channels 06, 16, and 70 \n\n4) Channels 06, 08, 72 and 77",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "1 GHz is equivalent to: \n\n1) 1000 000 000 Hz \n\n2) 1000 000 Hz \n\n3) 10000 000 000 Hz \n\n4) 100 000 Hz",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "When a DSC-message of the 'distress' category is received, in order to start distress alert communication in so far as not indicated in the alert, you will switch to VHF channel: \n\n1) 13 \n\n2) 16 \n\n3) 67 \n\n4) 85",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "According to the rules of GMDSS vessels equipped for all sea areas have to be provided with: \n\n1) 156.3 KHz EPIRB \n\n2) 121.5/243.0 MHz VHF EPIRB \n\n3) 406.0 MHz Cospas-Sarsat EPIRB \n\n4) 1.6 GHz Inmarsat/DSC EPIRB",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "After confirmation that there is no other radio-traffic, we call on a VHF working channel of a coast-station. When you don't get any reply: \n\n1) You must wait 1 minute minimum before repeating your call \n\n2) You can repeat your call immediately \n\n3) You must wait 5 minutes before repeating the call \n\n4) You must wait 3 minute minimum before repeating your call",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "To announce an important navigational -or meteorological warning via the VHF-installation, one should use the: \n\n1) Safety call \n\n2) Distress call \n\n3) Urgency call \n\n4) Individual call",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "On area A4 the function \"Transmission of ship to shore distress alerts\" is mainly based on: \n\n1) The use of HF DSC and INMARSAT Epirbs \n\n2) The use of HF DSC and COSPAS SARSAT Epirbs \n\n3) The use of MF DSC and INMARSAT Epirbs \n\n4) The use of VHF DSC and VHF Epirbs",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "With an Inmarsat-C terminal the option 'PSTN' for addressing is available. This option: \n\n1) Have the operator read the message by phone \n\n2) Delivers the message as a fax \n\n3) Is to deliver a message by telephone via a modem on the computer of the suscriber \n\n4) Delivers a message as a telegram",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "If requested by a coastal radio station to participate in a rescue operation, what is the most important information you may give? \n\n1) Your vessel's own cargo owner \n\n2) Your crews nationality \n\n3) Your vessel's destination \n\n4) Your vessel's position, name, call sign and speed",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "The display of the DSC-controller on board is showing the following lines: TX call:Selective\nto: 02114200 Category:RoutineUSB:telephony DSC Tx 2189.5 kHz\nsave>send  This DSC-message must be transmitted in the mode: \n\n1) F1B \n\n2) H3E \n\n3) J3E \n\n4) G3E",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The altitude effect of the reflection of radio waves in the ionosphere on the transmission range also depends on: \n\n1) The equipment used \n\n2) The day/night situation \n\n3) The sensitivity of the receiver \n\n4) The position of the pre-selector tuning-button",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "The relay of a distress-call by an RCC for coast-station begins with: \n\n1) PAN PAN (3x) \n\n2) Distress (3X) \n\n3) MAYDAY RELAY (3x) \n\n4) MAYDAY (3x)",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Which means of communication is used by the NAVTEX system ? \n\n1) VHF \n\n2) E mail \n\n3) Satellite \n\n4) MF",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "\"On area A1 the function 'Reception of shore to ship distress alerts' is mainly based on:\"\n\n1) The use of VHF DSC \n\n2) The use of SART transponders \n\n3) The use of MF DSC \n\n4) The use of SARSAT COSPAS Epirbs",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Under GMDSS rules the trading area A1 can be considered to be:\n\n1) Within range of MF coast radio stations. \n\n2) Within range of VHF coast radio stations. \n\n3) Within the coverage of INMARSAT. \n\n4) Polar region.",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Which of the following frequency bands would most likely provide reliable communications between two stations that are 100 miles apart?\n\n1) The Very High Frequency (VHF) band. \n\n2) The High Frequency (HF) band. \n\n3) The Medium Frequency (MF) band \n\n4) The Low Frequency (LF) band.",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "By non-reduced transmitting power in VHF is meant in a power between:\n\n1) 25 - 50 watt \n\n2) 1 - 6 watt \n\n3) 5 - 10 watt \n\n4) 6 - 25 watt",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "When during transmitting the display of a radiotelephone-installation shows a decrease in transmitting power it is: \n\n1) An indication of aerial problem \n\n2) An adjustment of the semi-duplex transmitting power \n\n3) An indication of choosing a wrong channel \n\n4) An automatic adjustment of the chosen transmitting mode",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "On the MF/HF transmitter-receiver there is a sensitivity control. Another name for this is: \n\n1) AF-gain \n\n2) RF-gain \n\n3) AGC-gain \n\n4) LF-gain",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "A frequency is measured in: \n\n1) Seconds \n\n2) Micro-seconds \n\n3) Hertz \n\n4) Metres",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Your vessel is not in distress and not taking part in a distress operation. How would you impose radio silence on vessels which are interfering the distress traffic? \n\n1) Seelonce Mayday \n\n2) Seelonce Pan \n\n3) Seelonce Securite \n\n4) Seelonce Distress",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Define the class of emission H3E: \n\n1) Radiotelephony - Single sideband full carrier \n\n2) Radiotelex and DSC - Frequency shift keying of carrier with error correction \n\n3) Radiotelephony - Frequency modulation \n\n4) Radiotelex and DSC - Frequency shift keying of sub-carrier with error correction",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Which class of emission is used for MF radio telephony transmissions? \n\n1) F3E \n\n2) J3E \n\n3) G3E \n\n4) H3E",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "In accordance with GMDSS rules, the frequency 2187.5 kHz is used for: \n\n1) Routine message \n\n2) On scene communication \n\n3) Distress alerting \n\n4) Distress traffic",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Which wavelength applies to a frequency of 2000 kHz? \n\n1) 15 mtr \n\n2) 15000 mtr \n\n3) 1500 mtr \n\n4) 150 mtr",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Notices to all vessels of a certain shipping-company are sent via the Inmarsat by an EGC-service. This EGC-service is called: \n\n1) FleetNet \n\n2) ShipNet \n\n3) SafetyNet \n\n4) Satnet",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The Inmarsat-satellites are located: \n\n1) Between Lat 70 degree N and 70 degree S \n\n2) Above the equator \n\n3) Alternatively above the poles and the equator \n\n4) In a geostationary orbit at approximally 1000 km. Altitude",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "The type of Inmarsat station A,B,C,M is recognized by \n\n1) The first four digits of the identification \n\n2) The first two digits of the identification \n\n3) The first digit of the identification \n\n4) Last digit of the identification",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "The squelch on the control panel of a VHF-sat serves to: \n\n1) Adjust the receivers volume\n\n2) Adjust the sound level of the signal received \n\n3) Adjust the proportion of atmospheric noise in receiving the spoken word \n\n4) Adjust the threshold level for admitting signals and refusing noise ",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Code signals concerning requests and general information on medical matters normally consist of: \n\n1) Letter M plus two other letters. \n\n2) Letter P plus two other letters. \n\n3) Letter H plus two other letters. \n\n4) Letter D plus two other letters.",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Regular 'updating' of a ships' position in an Inmarsat-C installation is necessary \n\n1) To keep to the correct Inmarsat-region \n\n2) To have the correct position in case of accidents \n\n3) To enter the correct data to the disk antenna \n\n4) To inform the satellite of ships position",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Automatic amplifier regulation is used for the following reasons: \n\n1) With bad weather the signal is amplified \n\n2) With strong incoming signals distortion is reduced \n\n3) With weak incoming signals distortion is reduced \n\n4) With absence of incoming signals noise is reduced",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Every vessel equipped according to the rules of GMDSS must be provided with: \n\n1) HF radio telephony installation \n\n2) DSC listening watch receiver for 2187.5 Hz \n\n3) MF radio telephony-installation \n\n4) Navtex-receiver",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Regular 'updating' of a ships' position in an Inmarsat-C installation is necessary \n\n1) To have the correct position in case of accidents \n\n2) To keep to the correct Inmarsat-region \n\n3) To enter the correct data to the disk antenna \n\n4) To inform the satellite of ships position",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Code signals concerning requests and general information on medical matters normally consist of: \n\n1) Letter P plus two other letters. \n\n2) Letter M plus two other letters. \n\n3) Letter H plus two other letters. \n\n4) Letter D plus two other letters.",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Automatic amplifier regulation is used for the following reasons: \n\n1) With bad weather the signal is amplified \n\n2) With strong incoming signals distortion is reduced \n\n3) With weak incoming signals distortion is reduced \n\n4) With absence of incoming signals noise is reduced",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Every vessel equipped according to the rules of GMDSS must be provided with: \n\n1) HF radio telephony installation \n\n2) DSC listening watch receiver for 2187.5 Hz \n\n3) MF radio telephony-installation \n\n4) Navtex-receiver",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "An Inmarsat-C terminal is suitable for: \n\n1) Store and forward message \n\n2) Telephony, fax and data \n\n3) Telex only \n\n4) Telephony, telex, fax and data",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "If one wants to transmit a weather report with an Inmarsat-C terminal one should use the following address: \n\n1) Sitrep \n\n2) 41 \n\n3) Meteorological Center \n\n4) OBS +",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Long distance communication in the HF-bands depends on: \n\n1) Satellites \n\n2) Ground wave \n\n3) Ionisation layers \n\n4) Weather conditions",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "\"On area A2 the function 'Transmission and reception of on scene communications' is mainly based on:\" \n\n1) The use of VHF DSC \n\n2) The use of MF DSC \n\n3) The use of SART transponders \n\n4) The use of MF and/or VHF R/T",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "What is the fundamental purpose of a coast radio station? \n\n1) To provide continuous DSC coverage \n\n2) To coordinate search and rescue communications. \n\n3) To automatically connect a vessel placing an INMARSAT call with the station being called. \n\n4) To provide a delivery service for ships with routine, safety, urgency or distress message traffic",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The identification of a coast station is composed as follows: \n\n1) 00 followed by an MMSI-number \n\n2) 00 followed by an MID-number and station number \n\n3) 00 followed by an MID-number \n\n4) 33 Followed by the MID number",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "What is the required number of hours that a SART's battery must be able to operate the unit in the standby mode? \n\n1) Eight (8) hours\n\n2) Forty-eight (48) hours \n\n3) Four (4) days  \n\n4) Three (3) days",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "The aerial system of an Inmarsat-C terminal consist of: \n\n1) A dish aerial \n\n2) A rod aerial \n\n3) A flexible wire aerial \n\n4) An omni-directional aerial",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "According to the rules of GMDSS all vessels have to be equipped with: \n\n1) A possibility to receive MSI \n\n2) On both sides an EPIRB \n\n3) At least three VHF radios \n\n4) A VHF in captains cabin",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "A VHF transmission range is mainly determined by: \n\n1) The ocean region \n\n2) The height of the aerial \n\n3) Whether it is radio-telephony, radio-telex or DSC \n\n4) The transmission power, propagation and the quality of the receiver",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "The effect of reflection of the radio waves in the ionosphere on the range depends on: \n\n1) The correct adjustment of the button band width \n\n2) The correct adjustment of the clarifier \n\n3) The amount of ionisation \n\n4) The correct adjustment of the dimmer",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "With help of DSC a ship wants to contact a coast-station to have a question for telephone call. One has to choose from the following DSC-frequencies \n\n1) TX: 8415.0 kHz RX: 8415.0 kHz \n\n2) TX: 8436.5 kHz RX: 8436.5 kHz \n\n3) Tx: 8414.5 kHz RX: 8414.5 kHz \n\n4) TX: 8415.0 kHz RX: 8436.5 kHz",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "You receive via the 8 MHz a DSC distress alert. The received DSC message is however distorted. The MMSI as well as the position are illegible. After listening at the 8 MHz telephone distress frequency, nothing is heard. This is because: \n\n1) Telephone signals in the same frequency band are generally weaker than DSC signals \n\n2) First an acknowledgement of a coastguard station must be received via the 8MHz \n\n3) You should have listened on VHF \n\n4) You should have listened on the 2182 kHz",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The DSC-controller displays the following: DOO: 246321000 CH16 ; S distress flooding After receiving this DSC message nothing more is received. Sending receipt on channel 16 does not give any response. One should first: \n\n1) Listen out on VHF channel 67 \n\n2) Send a DSC distress alert relay \n\n3) Inform the safety officer \n\n4) Send a DSC acknowledgement",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Define the acronym GMDSS. \n\n1) General Maritime Directories for Safety and Search \n\n2) General Mundial Distress and Safety System \n\n3) Global Maritime Distress and Safety System \n\n4) Global Mundial Direct System Safe",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "All designated SAR aircraft and civil aircraft carry equipment operating on the international aeronautical distress frequencies (amplitude modulation). The aeronautical distress frequencies are? \n\n1) 123.8 MHz and/or 247.6 MHz \n\n2) 243.1 MHz and/or 486.2 MHz \n\n3) 127.8 MHz and/or 349.6 MHz \n\n4) 121.5 MHz and/or 243.0 MHz",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "A message is send by the Inmarsat C-set. The land earth station will: \n\n1) Only send a positive delivery notification (PDN) to the sender if the sender requested, so in the send menu \n\n2) Automatically send a positive delivery notification (PDN) to the sender \n\n3) The sender has to confirm delivery by sending another separate message \n\n4) Never send a positive delivery notification (PDN) to the sender. The addressed will have to confirm the message through the ground-station and request for further information, if desired",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The batteries must be placed in a well ventilated place, so that: \n\n1) There is sufficient oxygen available for optimum working of the batteries \n\n2) The detonating gas can be discharged \n\n3) The production of detonating gas can be prevented \n\n4) The person can work in the compartment",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "When onboard channel 16 is used for a shore radio-connection, you always work: \n\n1) Duplex \n\n2) Semi-duplex \n\n3) Simplex \n\n4) On low power",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "The PTT-switch must be: \n\n1) Pressed in during speaking only to work duplex \n\n2) Pressed to listen \n\n3) Pressed in constantly to work simplex \n\n4) Pressed in during speaking only to work semi-duplex",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "A wire aerial for an MF/HF-transmitter must be suspended between isolators: \n\n1) To prevent contact with earth \n\n2) To make the way for aerial currents as long as possible \n\n3) To save energy \n\n4) To prevent burns when touching the aerial",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Define the class of emission F1B: \n\n1) Radiotelex - Frequency modulation \n\n2) Radiotelex and DSC - Frequency shift keying of carrier with error correction \n\n3) Radiotelephony - Phase modulation \n\n4) Radiotelex and DSC - Frequency shift keying of sub-carrier with error correction",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "What HF-band is generally suitable for long distance transmission if one of two stations is Located in twilight \n\n1) 16 MHz \n\n2) 22 MHz \n\n3) 12 MHz \n\n4) 4 MHz",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "The exact position of a 406 MHz Cospas-Sarsat EPIRB is eventually calculated by: \n\n1) The satellite \n\n2) The EPIRB \n\n3) Ship Manager \n\n4) LUT",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Identification of a ship station is amongst others done by an: \n\n1) MMSI-number \n\n2) MID-number \n\n3) MID-number, followed by the call sign \n\n4) Ship's code number",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "By frequency is meant: \n\n1) Time lapse of vibrations \n\n2) Number of vibrations per unit of time \n\n3) Number of vibrations \n\n4) Wave length of a loop",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "The propagation of radio-signals in the VHF-band is: \n\n1) Dependent on the hour of transmission (day or night) \n\n2) Dependent on the power emitted and the temperature of the atmosphere \n\n3) Almost rectilinear \n\n4) Straight",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Onboard the following message is received on the DSC controller: DOO: 245329000 CH16; S distress ack 244123000 What station sent the distress acknowledgement? \n\n1) None of the given \n\n2) 002453290 \n\n3) 244123000 \n\n4) 245329000",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "If one requires medical advice by means of an Inmarsat-C terminal one should use the following address: \n\n1) 32 \n\n2) Sick Seaman \n\n3) MED + \n\n4) Radiomedical",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "At the entrance to the space where batteries are stored on board the following notice must be fitted: \n\n1) Electrician only \n\n2) No entry with naked light and/or flame \n\n3) Keep access free \n\n4) Crew only",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "A distress alert sent by Inmarsat to an RCC is sent via: \n\n1) NCS \n\n2) The managers office \n\n3) LES \n\n4) LUT",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "If a ship in the MF-band wants to have a DSC-connection with a coast-station (no 'distress alert' or a test alert) the following frequencies are chosen: \n\n1) TX: 2177.0 kHz RX: 2189.5 kHz \n\n2) Tx: 2187.5 KHz RX: 2182 KHz \n\n3) TX: 2177.0 kHz RX: 2177.0 kHz \n\n4) TX: 2189.5 kHz RX: 2177.0 kHz",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Inmarsat Telex Service code '31' can be used: \n\n1) To ask for maritime inquiries \n\n2) When the coast-station is disfunctional \n\n3) When technical problems are experienced with the Inmarsat terminal \n\n4) To ask for medical assistance",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The transmitting power of the VHF is adjusted by setting: \n\n1) Squelch \n\n2) High/Low power \n\n3) Dual watch \n\n4) PTT",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "According to the rule of GMDSS, channel 70 is used for: \n\n1) Distress and urgency traffic \n\n2) Urgent communications \n\n3) Alerting \n\n4) Distress traffic",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "What is the emergency channel on VHF? \n\n1) Channel 21  \n\n2) Channel 69 \n\n3) Channel 09 \n\n4) Channel 16",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Distress MF communications should normally be operated: \n\n1) In J3E mode – on simplex basis \n\n2) In J3E mode – on duplex basis \n\n3) In G3E mode – on duplex basis \n\n4) In G3E mode – on simplex basis",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "With an Inmarsat-C installation there is the addressing-option 'special'. Via this option: \n\n1) You can deliver a message via a special telegram \n\n2) Give one of Inmarsat's 'special access codes' \n\n3) You can plan a message to be delivered at a special time \n\n4) You can send a message by express delivery",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Which of the following two digits codes is used to obtain maritime assistance? \n\n1) 38 \n\n2) 32 \n\n3) 39 \n\n4) 37",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "When a satellite receives a 'distress alert' from a Cospas-Sarsat EPIRB, the relay of the 'distress alert' can be delayed because the satellite cannot immediately contact a: \n\n1) Coast station \n\n2) NCS before the satellite is actually seen by this ground station \n\n3) LES before the satellite is actually seen by this ground station \n\n4) LUT before the satellite is actually seen by this ground station",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "For a 'distress alert' via the DSC, the MF-band is used in the frequencies: \n\n1) TX: 2187.5 kHz RX: 2187.5 kHz \n\n2) TX: 2177.0 kHz RX: 2177.0 kHz \n\n3) TX: 2189.5 kHz RX: 2189.5 kHz \n\n4) TX: 500.0 kHz RX: 518.0 kHz",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The obligation to identify oneself when using VHF is: \n\n1) Only when sailing in a block area \n\n2) Always \n\n3) Only when sailing in restricted visibility \n\n4) Only when navigating by radar",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "The nationality of a ship can be determined by means of: \n\n1) MMSI \n\n2) Ships name, followed by the AAIC \n\n3) Call sign \n\n4) AAIC",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "For how long time should a COSPAS-SARSAT eprb be able to operate on its batteries? \n\n1) 12 hours \n\n2) 24 hours \n\n3) 96 hours \n\n4) 48 hours",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "How will you start a cancelling message after you send by mistake a distress call on your VHF DSC equipment \n\n1) 'All Stations - This is ""SAINT-ROMAIN""' \n\n2) 'SECURITE - All Stations - This is ""SAINT-ROMAIN""' \n\n3) 'PAN PAN - All Stations - This is ""SAINT-ROMAIN""' \n\n4) 'MAYDAY - All Stations - This is ""SAINT-ROMAIN""'",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "To inform ship of coast-stations messages, coast-stations give at fixed times: \n\n1) A list of the official identification numbers, for example the Maritime Mobile Service Identity (MMSI) \n\n2) A traffic list with the call-sign of the ships involved in alphabetical numerical sequence \n\n3) A list of all the messages for each vessel \n\n4) A list with the names of the ships involved spoken alphabetical numerical sequence.",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Radio waves used in satellite communication are not affected by ionosphere because: \n\n1) Their power is too high \n\n2) TDM-signals are used \n\n3) A disc aerial is used \n\n4) The frequency of the radio waves is too high",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "HF communication is usually provided by: \n\n1) Space wave \n\n2) Ground wave \n\n3) None of the above \n\n4) Sky wave",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "On area A4 the function 'Transmission and reception of on scene communications' is mainly based on: \n\n1) the use of HF/MF and/or VHF R/T \n\n2) the use of HF DSC \n\n3) the use of MF and/or HF R/T \n\n4) the use of SARSAT COSPAS Epirb",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "If messages are received which aren't intended for own ship: \n\n1) They must only be passed to the master \n\n2) They must not be used for any purpose \n\n3) They must be forwarded to the company \n\n4) They must be noted in the radio log book",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "The prescribed periodic tests of the radio set must be entered in: \n\n1) Equipment manual \n\n2) Manual maritime radio communication \n\n3) Radio Log \n\n4) Ship's deck log",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "The accuracy of an Inmarsat-E positioning-system is: \n\n1) 20 miles \n\n2) 20 meters \n\n3) 5 miles \n\n4) 200 meters",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "To receive distress alerting and MSI via an Inmarsat-C set vessels must have: \n\n1) SES or an EGC receiver \n\n2) MF/HF radio telex scanner with printer \n\n3) Suitable for 518 kHz NAVTEX receiver \n\n4) A radio officer on board",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The display of the DSC-controller on board is showing the following lines: RX: 002442000 ; Ch87; D Sellcall Routine We're asked to listen on: \n\n1) Channel Delta of the coast station \n\n2) VHF- channel 87 \n\n3) VHF- channel 16 \n\n4) Radio telephony-channel 7 in the 8 MHz band",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "The correct functioning of a DSC-modem can be checked by means of: \n\n1) Tester provided with the equipment \n\n2) The testing-mode of the ever present VHF-DSC-EPIRB \n\n3) The built-in test facility in the modem \n\n4) The obligatory monthly transmission from the RCC's",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "When discussing VHF, 'reduced transmitting power' means power between: \n\n1) 100 - 150 watt \n\n2) 6 – 25 watt \n\n3) 5 – 10 watt \n\n4) 0,5 – 1 watt",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Which radio frequency/channels are reserved for emergency communication? \n\n1) 2182 kHz/VHF channel 16 \n\n2) 2182 kHz/VHF channel 6 \n\n3) 2128 kHz/VHF channel 16 \n\n4) 2188 kHz/VHF channel 8",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The receiver of the Inmarsat-C installation, if the log-in procedure has been carried out, is turned on: \n\n1) RCC common channel\n\n2) NCS common channel  \n\n3) NCC information channel \n\n4) LES message channel",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "A distress-call received via RCC should: \n\n1) Always be given receipt \n\n2) Always be relayed \n\n3) Only be given receipt, if the master has confirmed that assistance indeed can be given \n\n4) Be given receipt, even when indubitably too distant from the distress case",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "You wish to send an e-mail using the Inmarsat-C installation. The message has to be composed in: \n\n1) The 400 protocol\n\n2) X25 \n\n3) National language of the LES \n\n4) ASCII ",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "On board they want to have a dial-phone call via Inmarsat with the Apollogracht. In the guides the following ID's are found for the Apollogracht:344320000, 424432000, 424432010, 424432020, 1300210, 36715. What ID should be chosen: \n\n1) 1300210 \n\n2) 344320000 \n\n3) 424432010 \n\n4) 424432020",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "In the Maritime Radio Traffic the order of priority is: \n\n1) Urgency traffic, distress traffic, safety traffic \n\n2) Distress traffic, urgency traffic, safety traffic \n\n3) Urgency traffic, safety traffic, routine traffic \n\n4) Safety traffic, distress traffic, urgency traffic",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "If a ship according to the rules of GMDSS is equipped with an MF/HF radio set a DSC listening watch must be kept on: \n\n1) 2182 kHz and channel 70 \n\n2) 2187.5 kHz, 8414.5 kHz and for instance 12577.0 kHz \n\n3) 8414.5 kHz and on at least one of the following DSC frequencies: 4207.5 kHz, 6312.0 kHz, 12577.0 kHz or 16804.5 kHz \n\n4) All DSC distress frequencies",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "The good operation in any location, whether the NAVTEX is working properly or not, can be checked using: \n\n1) Test transmissions specially broadcast for this purpose once a week \n\n2) A company test procedure \n\n3) A compulsory built-in alarm for defects \n\n4) A testing program built in for this purpose",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "\"On area A1 the function 'Reception of shore to ship distress alerts' is mainly based on:\" \n\n1) the use of VHF DSC \n\n2) the use of MF DSC \n\n3) the use of SART transponders \n\n4) the use of SARSAT COSPAS Epirbs",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Define the class of emission G3E: \n\n1) Radiotelex and DSC - Frequency shift keying of carrier with error correction \n\n2) Radiotelephony - Phase modulation \n\n3) Radiotelephony - Frequency modulation \n\n4) Radiotelex and DSC - Frequency shift keying of sub-carrier with error correction",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Under GMDSS which VHF channel is used for Digital Selective Calling (DSC)? \n\n1) Ch.06 \n\n2) Ch.13 \n\n3) Ch.70 \n\n4) Ch.16",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "How are the NAVTEX areas identified? \n\n1) By one digit \n\n2) By one letter \n\n3) By one lettre and one digit \n\n4) By two letters",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "On area A3 the function 'Transmission and reception of signals for locating' is mainly based on: \n\n1) the use of SART transponders \n\n2) the use of SARSAT COSPAS Epirbs \n\n3) the use of HF DSC \n\n4) the use of MF DSC",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "For how long time should a VHF survival craft transceiver be able to operate on its batteries? \n\n1) 6 hours \n\n2) 8 hours \n\n3) 12 hours \n\n4) 24 hours",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "By a 'geographical area call' in the DSC system is meant: \n\n1) A DSC- message for all vessels within a certain area from a position in the DSC message, and the degrees are given in northerly and westerly direction \n\n2) A DSC- message for all ships heading towards a certain geographical area \n\n3) A DSC- message for all vessels within a certain area marked by a reference position, given in the DSC message and the degrees are given in southerly and easterly direction \n\n4) A DSC- message for all ships in a particular ocean region",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "The rule for having a radio transmitter license is internationally laid down in: \n\n1) SOLAS \n\n2) Search and rescue treaty of Hamburg \n\n3) SRT certificate \n\n4) Radio Regulations",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "On area A1 the function 'Transmission of ship to shore distress alerts' is mainly based on: \n\n1) The use of VHF DSC \n\n2) The use of HF DSC \n\n3) The use of SART transponders \n\n4) The use of portable VHF",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "If a coast-station doesn't answer a call on a VHF working channel or doesn't send a reply signal: \n\n1) You can repeat your call immediately when convinced that no other radio traffic is interfered with \n\n2) You must call on another working channel \n\n3) You must call on distress channel \n\n4) You can repeat your call after 2 minutes",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "With an EPIRB: \n\n1) You must check the manufacturer of the battery \n\n2) You must check the working of the charger and check the loaded condition of the battery \n\n3) You must check the date the battery must be replaced \n\n4) You must check if it is attached properly to a railing with the required line",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "How many total frequencies are available for DSC distress alerting? \n\n1) One (1) \n\n2) Five (5) \n\n3) Two (2) \n\n4) Seven (7)",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Which radio frequency/channels are reserved for emergency communication? \n\n1) 2182 kHz/VHF channel 16 \n\n2) 2182 kHz/VHF channel 6 \n\n3) 2128 kHz/VHF channel 16 \n\n4) 2188 kHz/VHF channel 8",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The receiver of the Inmarsat-C installation, if the log-in procedure has been carried out, is turned on: \n\n1) RCC common channel \n\n2) NCS common channel \n\n3) NCC information channel \n\n4) LES message channel",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "A distress-call received via RCC should: \n\n1) Always be given receipt \n\n2) Always be relayed \n\n3) Only be given receipt, if the master has confirmed that assistance indeed can be given \n\n4) Be given receipt, even when indubitably too distant from the distress case",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "You wish to send an e-mail using the Inmarsat-C installation. The message has to be composed in: \n\n1) The 400 protocol \n\n2) X25 \n\n3) National language of the LES \n\n4) ASCII",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "The satellite of the Inmarsat-EPIRB system have: \n\n1) Geostationary orbits \n\n2) Equatorial orbit \n\n3) Polar orbits \n\n4) Geopolar orbits",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "A ship in distress should transmit the appropriate alarm signal followed by the distress call and message on one or all of the international distress frequencies. Which of frequencies is in accordance with the present recommendations? \n\n1) 550 kHz, 2367 kHz and 121.5 MHz \n\n2) 500 kHz, 2182 kHz and 156.8 MHz \n\n3) 550 kHz, 2182 kHz and 121.5 MHz \n\n4) 500 kHz, 2367 kHz and 243 MHz",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "A lead battery of 200 Ah, in accordance with the DIN-standard, must be able to supply: \n\n1) 1 ampere during 200 hours \n\n2) 6 ampere during 20 hours \n\n3) 10 ampere during 20 hours \n\n4) 200 ampere during 1 hour",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "On board one can use the reflections in the ionosphere by the right choice of: \n\n1) The mode of transmission \n\n2) The type of equipment \n\n3) The length of the aerial \n\n4) The time of transmission",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "You wish to send a DSC-message because of a m.o.b. situation and assistance by other ships is required. You have to choose the category: \n\n1) Distress \n\n2) Individual \n\n3) Safety \n\n4) Urgency",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "A polarisation of a radio wave is determined by: \n\n1) Length of the aerial \n\n2) Position of the aerial \n\n3) Height of the aerial \n\n4) Condition of the aerial",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "To get proper conversation discipline in maritime radio traffic: \n\n1) Communication should be done only as per company's prescribed schedule \n\n2) Only after permission by captain, to send and/or receive on a VHF-channel pointed out the master \n\n3) Only necessary radio conversations are made in a concise and businesslike way \n\n4) Every available VHF-channel should always be used",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "For how long time should a SART transponder be able to operate in the active mode? \n\n1) 96 hours \n\n2) 6 hours \n\n3) 24 hours \n\n4) 8 hours",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "A 'Standard Format for Search and Rescue Situation Reports' (SITREPs) should be used by vessels in distress. The SITREP can be compiled as a short form (urgent essential details). Which of the following information shall be included when using the 'short form'? \n\n1) Weather on-scene. \n\n2) Cargo information. \n\n3) Position. \n\n4) Oil spill possibility.",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Polarisation of a radio wave means: \n\n1) The beam-angle of a transmitting aerial \n\n2) The direction of the electrical field \n\n3) The propagation speed of the signal \n\n4) The speed of the signal in polar regions",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "DSC-test transmissions may: \n\n1) Only be sent with MF/HF-installation on other frequencies than the DSC-distress frequencies, if the tele-command 'test' is used \n\n2) Only be sent on an MF-installation on frequencies other than the DSC-distress frequency \n\n3) Be sent by an MF-installation on the DSC-distress frequency \n\n4) Be sent by any installation",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "A DSC-notice should be sent on VHF-channel: \n\n1) 67 \n\n2) 16 \n\n3) 13 \n\n4) 70",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "To guarantee optimal reception of VHF-DSC-calls, every: \n\n1) DSC-symbol is sent twice and checked extra by Error Check Character \n\n2) DSC-report is sent twice, at least every second call is compared with the earlier received call \n\n3) DSC-calls are repeated until received \n\n4) DSC-symbol is checked on the right amount of 10, and then checked on the correct relation by Error Checked Character",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Which type of call will be sent by a ship in danger of capsizing and needing assistance from all vessels in her vicinity? \n\n1) Distress relay call \n\n2) Distress call \n\n3) Safety call \n\n4) Urgent call",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "EGC is short for: \n\n1) Emergency general ship call \n\n2) Exchange Group Call \n\n3) Enhanced Group Call \n\n4) Exchange Geographic Call",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "A DSC distress alert single frequency call attempt is awaiting acknowledgement: \n\n1) Automatically repeated after 1 to 1 and a half minutes \n\n2) Repeated manually when required \n\n3) Not repeated automatically \n\n4) Automatically repeated after 3 and a half to 4 and a half minutes",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Non distress calls on 2182 kHz and VHF channel 16 should not exceed: \n\n1) One minute. \n\n2) Five minutes. \n\n3) Three minutes. \n\n4) Two minutes.",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "SART is short for: \n\n1) Search and Rescue radar transmitter \n\n2) Search and rescue radar transponder \n\n3) Safety and radio telephony \n\n4) Safety and Rescue radar transmitter",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Via Inmarsat-C a message is sent to an Inmarsat-C mailbox with a positive delivery notification (PDN). The ground station will: \n\n1) Send no PDN's with messages intended for the mailbox \n\n2) Send a PDN, as soon as the message is collected from the mailbox \n\n3) Send a PDN, if the message has arrived in the mailbox \n\n4) Not send any PDN for this message",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "The prescribed test of an approved portable VHF radio set (portophone) must be done once a: \n\n1) Week \n\n2) Year \n\n3) Quarter \n\n4) Month",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "What is EPIRB an abbreviation for? \n\n1) Emergency Position Indicating Radio Beacon. \n\n2) Electronic Purpose If Rescue Begins. \n\n3) Electronic Pressure Indication Radar Buoy. \n\n4) Emergency Position Indication Radio Buoy.",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Modulation is: \n\n1) Deleting carrier wave \n\n2) Blending LF & HF signals \n\n3) Detecting frequency \n\n4) To enhance the side bands in relation to the carrier wave",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "The number of oscillations of a wave per seconds is called : \n\n1) Class of emission \n\n2) Wavelength \n\n3) Frequency \n\n4) Period",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "In maritime radio traffic sea area A1 is considered a sea area which: \n\n1) With the exception of sea area A3-A4 and within range of a HF radio station where continuous alarm is available \n\n2) Is not covered by any coast station \n\n3) With the exception of sea area A2-A3 within the range of a Cospas-Sarsat satellite where continuous alarm is available \n\n4) Is within radio traffic range of at least one VHF- coast station where continuous DSC-alerting is available",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "The number of frequencies on which a MF/HF-DSC distress alert multi-frequency call attempt can be transmitted is: \n\n1) 6 \n\n2) 5 \n\n3) 2 \n\n4) 3",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "1MHz is equivalent to: \n\n1) 100 000 Hz \n\n2) 1000 000 Hz \n\n3) 10 000 Hz \n\n4) 10 000 000 Hz",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "By \"collect call\" is meant: \n\n1) A group call \n\n2) An urgent call \n\n3) A call for account of the receiver \n\n4) A call to collect the charges in office",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Reflection of radio waves in the ionosphere depends on: \n\n1) The propagation speed of propagation\n\n2) The chosen mode of transmission \n\n3) The speed of the waves \n\n4) Sunspots ",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "The mode J2B is used: \n\n1) For radiotelex-traffic in the MF/HF band between the ship and shore stations \n\n2) In public broadcasting \n\n3) For telephone traffic in the MF/HF bands between ship and shore stations \n\n4) For urgent message transmitting and receiving",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The ship-shore HF-telephone-channel 2228 consists of the frequencies 22081.0 kHz and 22777.0 kHz. In case of manual operation, one should tune the receiver on: \n\n1) The common receiving frequency for the 22 mHz band \n\n2) 22777.0 kHz \n\n3) 2228 kHz \n\n4) 22081.0 kHz",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "The category of a DSC-call determines: \n\n1) For whom the message is destined \n\n2) How the rest of the call is to be composed \n\n3) The degree of priority \n\n4) How to conduct search and rescue",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Inter-ship traffic at sea should preferably take place on: \n\n1) VHF channel 70 \n\n2) VHF channel 10 or 13 \n\n3) VHF channel 77 or 72 \n\n4) VHF channel 06 or 08",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "What is MERSAR an abbreviation for? \n\n1) Merchant Ship Search and Rescue Manual. \n\n2) Merchant Radio Signal and Receiver. \n\n3) Merchant Ship Safety and Rescue. \n\n4) Maritime Emergency Radio Signal and Response.",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The DSC-controller display the following: DOO: 244562000 CH16 ; S distress sinking After receiving this DSC message the following is done immediately: \n\n1) Call the Chief officer \n\n2) Listen out on VHF channel 16 \n\n3) Send a \"distress alert relay\" \n\n4) Give a \"DSC-acknowledgement\"",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "A battery of 24 Volt supplies during 10 hours a current of 6 ampere. What is the capacity supplied: \n\n1) 48 Ah \n\n2) 144 Ah \n\n3) 60 Ah \n\n4) 240 Ah",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "On board a DSC-call is to be made in case of an OBS. Choose the category: \n\n1) Ship's business \n\n2) Urgency \n\n3) Safety \n\n4) Routine",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "The distress message is used when the vessel is threatened by a serious and imminent danger and is in need of immediate assistance. What is the telephony distress signal? \n\n1) MAYDAY \n\n2) SECURITE \n\n3) PAN-PAN \n\n4) RESCUE-RESCUE",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "On area A4 the function \"Transmission and reception of signals for locating\" is mainly based on: \n\n1) The use of MF DSC \n\n2) The use of SART transponders \n\n3) The use of HF DSC \n\n4) The use of SARSAT COSPAS Epirbs",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "The frequency 121,5 MHz is used for : \n\n1) INMARSAT E EPIRBS \n\n2) SART transponder \n\n3) COSPAS-SARSAT EPIRBS \n\n4) DSS VHF calls",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "The HF-band is in the frequency range: \n\n1) 30 - 300 GHz \n\n2) 3 - 30 GHz \n\n3) 3 - 30 KHz \n\n4) 3 - 30 MHz",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "What mode must be used on the MF/HF transmission, when transmitting a telex-message: \n\n1) F1B/J2B \n\n2) G3E \n\n3) H3E \n\n4) J3E",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "A distress alert on board may only be transmitted on explicit order of: \n\n1) The radio officer \n\n2) The captain \n\n3) The safety officer \n\n4) The navigating officer on duty",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "By DUAL WATCH in maritime VHF-communication is understood: \n\n1) Talking to two station at the same time \n\n2) The possibility to keep radio-contact with two or more stations simultaneously \n\n3) To keep a listening watch on two channels more or less simultaneously \n\n4) Automatically reduction of transmitting power",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "To choose the HF-band, the time difference between 2 stations: \n\n1) Is multiplied by the hour at the transmitting station \n\n2) Is irrelevant \n\n3) Is hardly relevant \n\n4) Is important",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Which of the following channels and modes should be used when initiating a distress alert transmission? \n\n1) Channel 70 DSC \n\n2) Channel 13 Radiotelephony and channel 16 DSC. \n\n3) Channel 6 Radiotelephony. \n\n4) Channel 6 DSC",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "What document gives permission to have the on board transmitting equipment? \n\n1) General operator license \n\n2) A Ship station license \n\n3) Operating certificate \n\n4) Safety certificate",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "The Urgency Message from a ship is used to notify other traffic of a situation where the ship is not in imminent danger, but where the development of the situation is uncertain and may need assistance in the near future. What is the telephony urgency message like? \n\n1) RESCUE-RESCUE \n\n2) MAYDAY \n\n3) PAN-PAN \n\n4) SECURITE",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Moored in a harbour, transmitting with a VHF is: \n\n1) Allowed in emergency only \n\n2) Not allowed \n\n3) Allowed in consultation with harbour master \n\n4) Always allowed",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Testing a SART is permitted: \n\n1) At sea, outside territorial waters, and in port or harbour \n\n2) Only in a port or harbour \n\n3) Only in the workshop \n\n4) Only at sea, outside territorial waters",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "The Inmarsat Maritime Communications Manual contains tables of: \n\n1) Inmarsat SES-ids \n\n2) Telephone country codes \n\n3) Radio telex frequencies of coast stations \n\n4) Company telephone numbers",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Sea area A4 is in maritime radio traffic sea area: \n\n1) Upto 12 miles of land \n\n2) With the exception of sea areas A1, A2 and A3, within the range of Inmarsat satellites, where continuous alarm is available \n\n3) Outside the sea areas A1, A2 and A3 \n\n4) Within VHF-radiotelephony-range of a coast station, where continuous DSC-alarm is available",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "The International Organisation which has developed GMDSS is: \n\n1) SARSAT-COSPAS \n\n2) ITU \n\n3) INMARSAT \n\n4) IMO",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "When on HF band a DSC distress alert is received, you have to listen to: \n\n1) The radio telephony distress frequency in the band in which the DSC distress alert was received \n\n2) 8414.5 kHz (DSC distress frequency in 8 MHz) \n\n3) 2182 kHz \n\n4) The radio-telex distress frequency in the band in which the DSC distress alert was received",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "The normal mode of operation for each coast station shall be indicated in: \n\n1) The ITU List of Ship Stations  \n\n2) The ITU List of Coast Station\n\n3) The ITU List of Radiodetermination and Special Services \n\n4) The ITU List of Call signs and numerical identities of station used by the maritime mobile and maritime mobile-satellite services",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "The sound level of the telephone in the telephone microphone is adjusted on the panel of i.g. an MF/HF radiotelephony installation with: \n\n1) RF-Gain \n\n2) Volume control \n\n3) Can not be adjusted, this is set by the manufacturer \n\n4) AF-Gain",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "An area within the radiotelephone coverage of at least one VHF coast station in which continuous DSC alerting is available is called: \n\n1) coastal area \n\n2) A2 \n\n3) ASN1 \n\n4) A1",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Secrecy in maritime radio traffic means that: \n\n1) Received messages which aren't intended for own ship are not used \n\n2) Received messages are not to be disclosed to other seafarers \n\n3) The speaker of the VHF is to be surged off during private conversations \n\n4) The VHF may only be operated by certificate holders who have signed a statement of secrecy",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "A SART must, when the vessel sinks: \n\n1) Should be left on board \n\n2) Be taken by the crew to the rescue-boat and turned on manually \n\n3) Automatically released and then automatically activated \n\n4) Automatically be released from the vessel and be turned on by equipment onboard the SART-units",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "The first time you send a DSC distress alert via the HF-band, you prefer the: \n\n1) 22 MHz band \n\n2) 12 MHz band \n\n3) 8 MHz band \n\n4) 16 MHz band",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Inmarsat Telex Service code '33' can be used: \n\n1) When the coast-station is disfunctional\n\n2) To ask for maritime enquiries \n\n3) To ask for radio medical advice \n\n4) When technical problems are experienced with the Inmarsat-terminal ",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "If one wishes to make a collect call from a vessel to a shore subscriber, one must: \n\n1) Request for a collect call \n\n2) Request for telephone message stating name, address and telephone number \n\n3) Inform the telephone number on whom to charge the call \n\n4) Request for a personal call",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "A message is sent to a fax-machine. However the message cannot be delivered by the land earth station. The land earth station will: \n\n1) Will only send a non-delivery notification (NDN) to the sender if so requested by him \n\n2) Automatically send a non-delivery notification (NDN) to the sender \n\n3) Call the sender on telephone and inform \n\n4) Never send a non-delivery notification (NDN) message to the sender. The sender to verify if the message was received",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "On what wave band does the search and rescue radar transponder operate? \n\n1) 8 GHz \n\n2) 6 GHz \n\n3) 9 GHz \n\n4) 2182kHz",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "A ship equipped to sail in sea area A2 has at least: \n\n1) A MF radio telephony installation and MF radiotelex installation \n\n2) A MF radiotelex installation \n\n3) A HF radio telephony installation \n\n4) A MF radiotelephony installation",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Which media are used to receive MSI? \n\n1) All of the mentioned alternatives \n\n2) NAVTEX \n\n3) SafetyNET \n\n4) HF NBDP",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "A SART must be visible on the ship's radar from a distance of at least: \n\n1) 30 miles \n\n2) 5 miles  \n\n3) 50 miles \n\n4) 10 miles",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "A « MRCC » is: \n\n1) The master of a merchant ship who coordinates on scene search and rescue operations \n\n2) The master of a SAR unit which coordinates on search and rescue \n\n3) A search and rescue coordination centre \n\n4) A coast station",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "The frequency 156,8 MHz is used for: \n\n1) DSC calls \n\n2) NAVTEX \n\n3) SARSAT COSPAS EPIRBs \n\n4) VHF channel 16",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "On which channel must a ship maintain a continuous watch when sailing in area A1? \n\n1) 70 \n\n2) 2182 \n\n3) 13 \n\n4) 2187.5",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "\"RECEIVED MAYDAY\" is used in a: \n\n1) When received a weather report \n\n2) Receipt of a distress alert \n\n3) Distress alert \n\n4) Supplementary receipt on a distress alert",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "What ships does GMDSS apply to? \n\n1) All vessels trading beyond national waters \n\n2) All vessels above 800GRT on International voyages \n\n3) All ships covered by Chapter IV of SOLAS I.e., all cargo ships of 300GRT and above and all passenger ships on International voyages \n\n4) Applies to tankers of 1599grt and above and all passenger ships trading either coastwise or internationally",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "On area A3 the function \"Reception of shore to ship distress alerts\" is mainly based on: \n\n1) The use of VHF DSC and NAVTEX \n\n2) The use of SARSAT COSPAS Epirbs and NAVTEX \n\n3) The use of MF DSC and INMARSAT C SAFETYNET \n\n4) The use of HF DSC and INMARSAT C SAFETYNET",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "The different layers in the ionosphere, important for radio propagation, are effected by: \n\n1) The Sun \n\n2) Direction of the antenna \n\n3) The distance between the transmitter and the receiver \n\n4) The weather-conditions",
                           "https://t.me/picturesforbo/197", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)



        print(f"Вопросы для теста '{name}' успешно добавлены.")

    except Exception as e:
        print(f"Ошибка при добавлении теста {name} или вопросов к нему: {e}\n{traceback.format_exc()}")


async def main():
    await add_specific_test_questions()
    print("Данные для специфического теста успешно обработаны.")


if __name__ == "__main__":
    asyncio.run(main())