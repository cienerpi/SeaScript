import asyncio
import traceback
from database_manager import add_test, add_question


async def add_specific_test_questions():
    # Определяем название и отдел только для интересующего нас теста
    name = "CES 6 General Cargo (Management)"
    department = "deck"

    try:
        test_id = await add_test(name, department)
        # После добавления теста, добавляем к нему вопросы напрямую
        await add_question(test_id,
                           "When should a crew member joining a ship for the first time be given some training instructions in the use of the ship's fire-fighting appliances? \n\n1) As soon as possible but not later than 2 weeks after he joins the ship. \n\n2) As soon as possible. \n\n3) As soon as possible but not later than 2 days after he joins the ship. \n\n4) As soon as possible but not later than 24 hours after he joins the ship",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "The receiver of the Inmarsat-C installation, if the log-in procedure has been carried out, is turned on:? \n\n1) NCC information channel. \n\n2) NCS common chanel. \n\n3) RCC common channel. \n\n4) LES message channel.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "On area A1 the function ''''Transmission ans reception of signal for locating '''si mainly bases on.:? \n\n1) the usw of VHF DSC. \n\n2) the use of SARSAT COSPAS Epirbs. \n\n3) yhe use of INMARSAT Epirbs. \n\n4) the use of SART transponders.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "The recommended connection between antenna and VHF is:? \n\n1) Electric cable. \n\n2) Band cable . \n\n3) Coaxial cable. \n\n4) Three vein cable.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "The traffic list of a coast-station is a list of: \n\n1) Call-signs of ships for which a radio- telephone call, a telegram or another call is intended. \n\n2) Names of ships which, on behalf of safety at sea, are being routed by a traffic control system. \n\n3) Pertiented navigation - and weather information. \n\n4) Name of ship's scheduled for berthing.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "On an oil tanker, are there any restrictions as to the maximum amount of treated water that originates from cargo spaces that has passed through a bilge water separator that can be discharged? \n\n1) Maximum is 60 litre pr nautical mile and total is 1/30000 part of full cargo on the ballast voyage. \n\n2) Maximum is 30 litre pr nautical mile and total is 1/30000 part of full cargo on the ballast voyage. \n\n3) Maximum is 60 litre pr nautical mile and total is 1/10000 part of full cargo on the ballast voyage. \n\n4) There isn't any restrictions of pumping sludge from ships outside special areas.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Which statement best describes what happens to the vessel symbol on an ECDIS set in North-up, true motion mode? \n\n1) Vessel is stopped on the screen, land moves relative. \n\n2) This is a feature only seen on a radar display. \n\n3) Vessel symbol moves across the screen. \n\n4) Vessel symbol shows the heading fixed vertically on the screen.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Who will have the authority to take charge and make appropriate decisions in the event of a vessel emergency when transiting the Panama Canal? \n\n1) The ship's company. \n\n2) The ship's Master. \n\n3) The Master and Pilot will agree the best 2 course of action to be taken to resolve the emergency situation.. \n\n4) The Panama Canal Authority.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "The training manual shall contain instructions and information in easily understood terms and illustrated wherever possible. Which of the following objects have to be explained in detail in the manual according to present regulations?? \n\n1) Donning of lifejackets and immersion suits.\n\n2)  Donning of fire protection clothing. \n\n3)  Handling of stowaways. \n\n4) Starting of Main Engine.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Which word will precede a routine message? \n\n1) PAN PAN. \n\n2) No specific word will precede a routine message. \n\n3) ROUTINE. \n\n4) MAYDAY.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Which of these tasks are performed as part of the SSA?? \n\n1) Train shipboard personnel in their security duties.. \n\n2) Implement measures to address weaknesses in ship security. \n\n3) Assess the likelihood and potential consequences of security incidents. \n\n4) Assign security duties to ship personnel.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "For a ship operating or calling in US waters, COTP can request (OPA-90)? \n\n1) Maximum one drill a year. \n\n2) Participation in all announced drills \n\n3) Maximum two drills a year. \n\n4) Unannounced drills at any time.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "If a coast-station doesn't answer a call on VHF working channel or doesn't send a reply signal? \n\n1) You must call on another working channel. \n\n2) You can repeat your call after 2 minutes \n\n3) You must call on distress channel. \n\n4) You can repeat your call immediately when convinced that no other radio traffic is interfered with.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "RECEIVED MAYDAY is used in a: \n\n1)Supplementary receipt on a distress alert \n\n2) Receipt of a distress alert. \n\n3) Distress alert.,\n\n4) When received a weather report.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "For security purposes, the IMDG Code should be read in conjunction with the: \n\n1) IMO NVIC 24 and 46 CFR 2.05 \n\n2) Chapter V of SOLAS and Annex II of MARPOL. \n\n3) Chapter XI-2 of SOLAS and Part A of the ISPS Code,\n\n4) Part B of the ISPS Code and Chapter II of the Maritime Transport and Offshore Facilities Act.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "The transmitting power of the VHF is adjusted  by setting: \n\n1) Squelch \n\n2) PTT. \n\n3) Dual watch,\n\n4) High/Low power.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Which word will precede a safety message? \n\n1) SECURITE \n\n2) SAFETY. \n\n3) PAN PAN. \n\n4) URGENT.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Under most circumstances, how will communication be carried out between a ship and a SAR helicopter? \n\n1) On 410KHz \n\n2) On VHF Ch 16. \n\n3) On 121.5 MHz. \n\n4) On VHF Ch 70.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "A SART must, when the vessel sinks: \n\n1) Should be left on board. \n\n2) Automatically released and then 3 automatically activated \n\n3) Be taken by the crew to the rescue-boat and turned on manually. \n\n4) Automatically be released from the vessel and be turned on by equipment onboard the SART-units.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "The ID of an Inmarsat M station on board starts with: \n\n1) 4. \n\n2) 3 \n\n3) 1. \n\n4) 6.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "The OPA-90 notification requirement is : \n\n1) Notify as soon as you have knowledge of any spill, or threat of a spill. \n\n2) Notify only if you mean that own vessel might be responsible \n\n3) Notify only if you mean that own vessel might be tracked and charged. \n\n4) Notify as soon as you have knowledge of a spill exceeding 10 gallons of oil.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "What is the best way to avoid pollution from small oil-spills aboard a ship? \n\n1) Have sawdust reade for use. \n\n2) Contain any oil-spill onboard the ship \n\n3) Have dispersing chemical ready for use in case of oil-spill. \n\n4) Rig an oil boom around the ship.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "A DSC-message of the ""safety"" category is received from another vessel on VHF channel 70. Conforming to the GMDSS rules, for the continuation of the safety traffic, you must change to VHF-channel:: \n\n1) 70. \n\n2) 85 \n\n3) 16. \n\n4) 07.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Via Inmarsat-C a message is sent to an Inmarsat-C mailbox with a positive delivery notification (PDN). The ground station will:: \n\n1) Not send any PDN for this message. \n\n2) Send a PDN, as soon as the message is collected from the mailbox \n\n3) Send no PDN's with messages intended for the mailbox1. \n\n4) Send a PDN, if the message has arrived in the mailbox.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "DCS-test transmissions may: \n\n1) Be sent by an MF-installation on the DSC- distress frequency. \n\n2) Only be sent with MF/HF-installation on other frequencies than the DSC-distress 2 frequencies, if the tele-command 'test is used \n\n3) Only be sent on an MF-installation on 3 frequencies other then the DSC-distress frequency. \n\n4) Be sent by any installation.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "New MARPOL regulations came into effect from July 93 stating that the oily water separator which was previously certified for 100 ppm be changed to:: \n\n1) 50 ppm. \n\n2) 15 ppm \n\n3) 10 ppm. \n\n4) 25ppm.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "You are proceeding along a narrow channel behind another vessel. You have a higher speed and have signalled your intention to the vessel ahead that you intend to overtake it on its port side. The vessel responds with this sound signal. What does it mean?: \n\n1) This is a signal intended for another 4 vessel or shore station. It is nothing to do with our vessel. \n\n2) That the vessel does not agree with my proposed manoeuvre \n\n3) That the vessel is indicating its agreement with my proposed manoeuvre. \n\n4) That the vessel suggests I overtake on the starboard side instead.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "A distress alert has accidentally been sent with the Inmarsat-C installation. One should now:: \n\n1) Turn off the transmitter. \n\n2) Wait until an RCC-reports \n\n3) Call the manager. \n\n4) Make contact with an RCC.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "The bridge wheelman has not reported for duty and there is a suspected ""Man Overboard"" situation on your vessel. The ship has been searched and there is one seaman missing? The vessel turns round and retraces the course back, calling for assistance from other vessels in the vicinity. What should be the focal point for any search pattern to be established? \n\n1) Determine when the seaman was last sighted and concentrate the search round the course line between the last sighting and present position, taking into account any prevailing current. \n\n2) Determine the drift and leeway of own ship and take this deviation from track into account on the return course. The search should focus around this return track back to the last sighted position \n\n3) The last sighted position should be the focal point of any search pattern and all ships should keep a good lookout in that vicinity, moving outwards to the present position. \n\n4) The focus of the search should be from the present position as he probaby went overboard when proceeding to the bridge for his watch.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "On the MF/HF transmitter-received there is a sensitivity control. Another name for this is: \n\n1) AGC-gain \n\n2) RF-gain. \n\n3) LF-gain. \n\n4) AF-gain.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "For which of the following ships. is the MARPOL convention applicable? \n\n1) For all vessels except passenger vessels \n\n2) For all vessels expect those engaged in coastal trade. \n\n3) For all listed vessels. \n\n4) Ror tankers and other vessels carrying persistens oil as cargo.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "What radar device assists in the detection and location of a survival craft? \n\n1) AIS beacon. \n\n2) EPIRB beacon \n\n3) A personal locator beacon. \n\n4) SART beacon.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "The mandatory color of a hand flare is: \n\n1) Red \n\n2) Green. \n\n3) Yellow. \n\n4) White.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "How are the effects of squad seen on a moving vessels? \n\n1) There will be a change of draught and a reduction in the speed. \n\n2) There will be a reduction of the vessel's underkeel clearance and a possible change of trim. \n\n3) Heel can result on a vessel with a large block coefficient and a speed reduction \n\n4) There will be an increase in the vessels draught while moving through the water",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           " ""Own-ship"" is to leave a crowded anchorage heading in the ""way out"" direction as illustrated. The ship has a right-handed propeller and conventional rudder. What would be the safest manoeuvre? \n\n1) Full ahead, rudder hard to port \n\n2) Full ahead, rudder hard to starboard \n\n3) Back out dead slow then full astern, transverse thrust should cant the bow to starboard. If the ship steers astern use port rudder \n\n4) Rudder hard to starboard, full ahead. Rudder hard to port, full astern. Repeating this manoeuvre until the turn has been made.",
                           "https://t.me/picturesforbo/71", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Which one of the listed requirements regarding service and maintenance of life- saving appliances correspond to present regulations?: \n\n1) Maintenance and repair of all life saving equipments shall be carried out by the certified ship staff only \n\n2) At least one member of the crew shall hold a repairman certificate for life- saving equipment \n\n3) Maintenance and repair of all the life- 2 saving equipments will be carried out ashore in work shop only \n\n4) Instructions for onboard maintenance of life-saving appliances in accordance with the regulations shall be provided",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "The prescribed test of EPIRB. SART and portable VHF radio set be entered in: \n\n1) Ship's radio log \n\n2) Radio equipment manual. \n\n3) Equipment survey. \n\n4) Maintenance manual.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "A DSC distress alert single frequency call attempt is awaiting acknowledgement:: \n\n1) Repeated manually when required \n\n2) Automatically repeated after 3 and a half to 4 and a half minutes \n\n3) Automatically repeated after 1 to 1 and a half minutes \n\n4) Not repeated automatically",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Is drugs are discovered onboard your ship... \n\n1) Notify the authorities after you arrive at the next port of call. \n\n2) Disembark crew and passengers as quickly 3 as possible at the next port of call so the authorities can conduct their investigation. \n\n3) Ensure the witness to the discovery signs your incident report. \n\n4) Write a report a few days after the event and describe everything that occurred.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "A message is sent to a fax-machine. However the message cannot be delivered by the land earth station. The land earth station will: \n\n1) Call the sender on telephone and inform \n\n2) Never send a non-delivery notification 3 (NDN) message to the sender. The sender to verify if the message was received \n\n3) Will only send a non-delivery notification 2 (NDN) to the sender if so requested by him \n\n4) Automatically send a non-delivery notification (NDN) to the sender",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Who is responsible for keeping the required official publications onboard? \n\n1) The master \n\n2) The owner \n\n3) The authorities. \n\n4) The radio officer",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "If requested by a coastal radio station to participate in a rescue operation, what is the most important information you may give? \n\n1) Your crews nationality \n\n2) Your vessel's position, name, call sign and speed \n\n3) Your vessel's destination \n\n4) Your vessel's own cargo owner",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "What should you do with the ashes from your vessels incinerator which had burned garbage containing plastics? \n\n1) Discharge at sea providing you are more than 25 miles offshore \n\n2) Discharge at sea providing you are more than 12 miles offshore \n\n3) Discharge to a shore facility only \n\n4) Discharge at sea providing you are not in any river or estuary",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "New MARPOL regulations came into effect from July 93 stating that the previous instantaneous rate of discharge of oil content (60 litters per nautical mile) was changed to:: \n\n1) 25 litters per nautical mile \n\n2) 10 litters per nautical mile \n\n3) 20 litters per nautical mile \n\n4) 30 litters per nautical mile",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "With a Relative Motion radar Display, what would an echo of a target with no trail indicate? Note that this is a target trail, not a vector: \n\n1) The target is on the same course and speed as own ship \n\n2) The target is on a collision course with own ship \n\n3) The target is stopped and making no way through the water \n\n4) The target is on a constant bearing and getting closer to own ship",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "On board passenger ships an abandon ship drill must be performed: \n\n1) Every month \n\n2) Every week \n\n3) Every three month  \n\n4) Every two weeks",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "One of the sailors needs urgent medical assistance. The VHF - call starts with: \n\n1) SOS (3x) \n\n2) Urgent (3x) \n\n3) PAN PAN (3x)  \n\n4) MAYDAY (3x)",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "A ship in distress should transmit the appropriate alarm signal followed by the distress call and message on one or all of the international distress frequencies. Which of frequencies is in accordance with the present recommendations? \n\n1) 550 kHz 2182 kHz and 121.5 MHz \n\n2) 550 kHz, 2367 kHz and 121.5 MHz \n\n3) 500 kHz, 2367 kHz and 243 MHz  \n\n4) 500 kHz, 2182 kHz and 156.8 MHz",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "With help of DSC a ship wants to contact a coast-station to have a question for telephone call. One has to choose from the following DSC-frequencies \n\n1) TX: 8415.0 kHz RX: 8436.5 kHz \n\n2) TX: 8415.0 kHz RX: 8415.0 kHz \n\n3) Tx: 8414.5 kHz RX: 8414.5 kHz  \n\n4) TX: 8436.5 kHz RX: 8436.5 kHz",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "You can reduce the need for security quards in certain areas by installing: \n\n1) Water  cannons \n\n2) Anti-intruder devices \n\n3) EMetal detectors  \n\n4) Vapour detectors",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "According to Rule 24 of the International Regulations for Preventing Collisions and the illustrated lights, how long is the tow likely to be? \n\n1) It is more than 50 metres but less than 200 metres \n\n2) At least 100 metres \n\n3) It exceeds 200 metres \n\n4) It is less than 200 metres",
                           "https://t.me/picturesforbo/99", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Where on the hull is the theoretical position of the hydrodynamic pivot point, when going ahead and turning? \n\n1) Normally varies dependant on the speed ahead \n\n2) Amidships \n\n3) 1/4 of vessel's length from the stern  \n\n4) 1/3 of the vessel's length from the bow.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "How many Radar Transponders (SART) are required to be carried onboard a ship for use in survival crafts? \n\n1) One on each side of the ship \n\n2) 2, one of which being capable of floating 3 free if the ship sinks \n\n3) Two on each side of the ship  \n\n4) One in each lifeboat",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "On area A3 the function ""Transmission and reception of signals for locating"" is mainly based on: \n\n1) the use of SARSAT COSPAS Epirbs \n\n2) the use of SART transponders \n\n3) the use of HF DSC  \n\n4) the use of MF DSC",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "What is the acronym FR 01? \n\n1) MSI \n\n2) Call sign \n\n3) AAIC  \n\n4) MMSI",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "What is definition on clean ballast as per MARPOL Annex 1?\n\n1) Ballast with an oil content of less than 1% \n\n2) There isn't any definition on clean ballast \n\n3) Ballast with an oil content of less than 45 ppm  \n\n4) Ballast with an oil content of less than 15 ppm",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "The Training Manual shall contain instructions and information on the life-saving appliances and the best method of survival. The training manual shall contain detailed explanations of crew duties in relation to emergency situations. Which of the following tasks or duties shall be included in the manual according to present regulations? \n\n1) The use of the ship's line throwing apparatus. \n\n2) The use of navigational equipment for 2 survival crafts. \n\n3) The use of escape routes and other escape methodes.  \n\n4) The use of surface to air visual signals to be used by survivors",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Most minor oil spills caused by: \n\n1) Major casualties \n\n2) Human error \n\n3) Unforeseeable circumstances \n\n4) Equipment failure",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "A wire antenna of 12 metres in length is probably: \n\n1) A Sat-C antenna \n\n2) An Inmarsat-antenna \n\n3) A MF/HF-antenna \n\n4) A VHF-antenna",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Which of the following is a ship MMSI? \n\n1) 2275300 \n\n2) 1227200 \n\n3) 22753000 \n\n4) 227530000",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Where is OPA-90 applicable? \n\n1) Withing 200 nm of US waters including Guam, Hawaii, Alaska and San-Juan \n\n2) 200nm off coast of California \n\n3) Within US waters \n\n4) 200 nm off US coast",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "At the entrance to the space where batteries are stored on board the following notice must be fitted: \n\n1) Keep access free \n\n2) No entry with naked light and/or flame \n\n3) Crew only \n\n4) Electrician only",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "MARPOL-Annex V. Disposal of garbage. Your vessel is in the Red Sea (Special Area) and the Chief Cook is requesting to have some food waste burned in the incinerator. Due to problems with incinerator, you decide to have the waste ground in the Grinder (Lump size max. 25 mm) and disposed off into the sea. Is this prohibited, if not, how far from nearest land is this legal? \n\n1) 3 miles \n\n2) This is prohibited \n\n3) 12 miles \n\n4) 25 miles",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "In a distress-situation a MF/HF-DSC transmission is used in the 8MHz frequency. In this case always: \n\n1) Ask the RCC for the frequency \n\n2) Turn on the right frequency \n\n3) Put in the MMSI number of the 3 coastguard on the DSC \n\n4) Indicate on what frequency communication will be continued",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "To get proper conversation discipline in maritime radio traffic: \n\n1) Only necessary radio conversations are made in a concise and businesslike way \n\n2) Communication should be done only as per company's prescribed schedule \n\n3) Every available VHF-channel should always be used \n\n4) Only after permission by captain, to send 4 and/or receive on a VHF-channel pointed out the master",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "The ship is in a shallow water starboard turn and the fore and aft Doppler log sensors show a sideways motion to port. Where would the theoretical pivot point be located? \n\n1) At a position on the centreline, about 1/6 of the ship's length forward of the rudder post \n\n2) At a position outside and forward of the hull \n\n3) At a position aft of amidships \n\n4) At a position outside and aft of the hull",
                           "https://t.me/picturesforbo/72", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "In the Inmarsat Maritime Communications Handbook one can find information about: \n\n1) Numbers of fax subscribers \n\n2) Radio telex commands \n\n3) 2 digit code telex services \n\n4) Ship's Inmarsat id's",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "The battery of a SART: \n\n1) Must be re-charged weekly \n\n2) Charged condition must be checked weekly \n\n3) Replaced monthly \n\n4) Must be replaced before the expiry date is exceeded",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "According to rule 12 of the International Regulations for Preventing Collisions, in the situation illustrated, which sailing vessel (A or B) must keep out of the way of the other? \n\n1) Sailing vessel A must keep out of the way of sailing vessel B. \n\n2) Sailing vessel B must keep out of the way of sailing vessel A. \n\n3) The upwind sailing vessel must keep out of the way of the downwind sailing vessel. \n\n4) Both sailing vessels are required to take avoiding action",
                           "https://t.me/picturesforbo/73", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Inmarsat Telex Service code ""31"" can be used: \n\n1) To ask for medical assistance \n\n2) To ask for maritime inquiries \n\n3) When technical problems are experienced with the Inmarsat terminal  \n\n4) When the coast-station is disfunctional",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Where on a vessel moving ahead through the water, is the most dangerous place for a tug to manoeuvre? \n\n1) The most dangerous position is when the tug is alongside the amidships section passing a line \n\n2) The most dangerous position is where the  tug approaches the stern of the larger vessel and enters into its associated positive pressure field \n\n3) The most dangerous position is where the tug approaches the bow, rounding the shoulder to pass a line\n\n4) There is no one position more dangerous than another, hydrodynamic effects are the same all around the hull",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Which of these precautionary measures can reduce the threat of piracy, if implemented? \n\n1) Plan to arrive at port at night. \n\n2) Turn off all of the ship's lights at night. \n\n3) Stay at least 15nm away from the shore \n\n4) Sail at full speed.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Give the meaning of the following symbol? \n\n1) Rocket parachute flares \n\n2) Survival craft distress pyrotechnic signals \n\n3) Radar transporter \n\n4) Epirb",
                           "https://t.me/picturesforbo/74", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "You are on a sailing vessel, underway in open water. This vessel is sighted on the starboard bow, on a steady bearing and the distance is closing. By the International Regulations for the Preventing Collisions at Sea, what action will you follow? \n\n1) Risk of collision is deemed to xist and, as the other vessel is on a steady bearing on my starboard side, I will maintain my course and speed  \n\n2) By Rule 18, a power-driven vessel underway shall keep out of the way of a sailing vessel. I will maintain my course and speed, but will continue to monitor situation to ensure the other vessel takes avoiding action \n\n3) This vessel is clearly a power-driven vessel and I anticipate that the bearing will therefore close and she will pass ahead at a safe distance  \n\n4) Risk of collision is deemed to exist and, as the other vessel is on a steady bearing on my starboard side, I am required to keep out of the way. I will make a broad alteration of course to starboard",
                           "https://t.me/picturesforbo/75", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "When a pollution incident occurs there is a plan for actions to be undertaken. State which of following priority sequences to be considered: \n\n1) Report-stop pumps clean up? \n\n2) Clean up report stop pumps? \n\n3) Stop pumps report - clean up? \n\n4) Stop pumps clean up report?",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "What are the three volumes of the IAMSAR Manual? \n\n1) AI Planning and Preparation II Control Ill Reference \n\n2) I Organization II Communications III Rescue Procedures \n\n3) A Command and Control B Communications C Rescue Procedures \n\n4) I Organization and Management II Mission Co-ordination III Mobile Facilities",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "The  capacity of a battery is expressed in: \n\n1) ampere x hours \n\n2) Watt x hours  \n\n3) volt x ampere  \n\n4) volt x hours",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Which option best describes what is meant by the Consistent Common Reference Point on a vessel. \n\n1) It is a position that the GPS aerial is in \n\n2) It is a point on the vessel common to all position related sensors \n\n3) It is a position that the radar scanner is in  \n\n4) It is a term associated the ECDIS time constant",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "A distress-call, onboard via RCC, may only be given Receipt if: \n\n1) The manager orders \n\n2) OSC from the RCC concerned invites the vessels  \n\n3) The O.O.W deems it necessary  \n\n4) The captain orders",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "The word CHANNEL is spelled conform the international phonetic alphabet: \n\n1) Cornelies, Hotel, Apple, November, November, Echo, Land \n\n2) Cornelies, Hotel, Alfa, November, 3 November, Echo, Lima  \n\n3) Charlie, Hotel, Able, November, 3 November, Echo, Liverpool \n\n4) Charlie, Hotel, Alfa, November, November, Echo, Lima",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Which one of the listed requirements regarding abandon ship drills corresponds to present SOLAS regulation? \n\n1) Each lifeboat shall be launched, and maneuvered in the water with its assigned crew at least once every three months during an abandon ship drill \n\n2) Drills shall be conducted when the ship is in a harbour  \n\n3) All lifeboats shall be lowered during drills  \n\n4) On ships on short international voyages,each lifeboat shall be launched and maneuvered in the water at least every six months",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "What does the abbreviation SOLAS mean? \n\n1) International Rules for Safe Ocean Lines and Sailing routes \n\n2) International Convention for the Safety of Lives at Sea \n\n3) International Conference for Security of Loads aboard Ships \n\n4) International Agreement for Security of 4 Load and Ships",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Which one of the listed items has to be included in a distress message? \n\n1) Destination \n\n2) Last port of call  \n\n3) Identification og the ship  \n\n4) Weather in immediate vicinity.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "What is the priority for the ship's management team when fire breaks out? \n\n1) The ship's management team must call the nearest fire brigade and police station \n\n2) The ship's management team must fight the fire and then call the fire teams \n\n3) The ship's management team and the crew must evocuate the ship  \n\n4) The ship's management team must organise the fire teams and then the teams hove to rescue missing personnel",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "What possible reason could there be for the identification mark associated with a Racon not being visible on the radar screen? \n\n1) All of the suggested answers. \n\n2) The radar may be suppressing the mark with application of the Interference Rejection control. \n\n3) The racon may not be transmitting a pulse \n\n4) The transmitted radar frequency may not trigger the Racon transmitter",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "For what period of time is the protection and environment committee elected? \n\n1) 3-4  years \n\n2) 1-2 years \n\n3) 5-6 years  \n\n4) 8 years",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "According to the IAMSAR Manual, what is the expected survival time for a person in water of temperature over 20 degrees Celsius? \n\n1) Between 18-24 hours depending upon their size \n\n2) Less than 12 hours if they have little body fat \n\n3) Indefinite, depending on fatigue state  \n\n4) Less than 24 hours because of hypothermia",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "What device can be used by a tug to get a line aboard a disabled vessel in bad weather, when it is dangerous for the tug to get too close? \n\n1) A cannon line \n\n2) A heaving line \n\n3) A missile line  \n\n4) A rocket line",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Only search vehicle compartments where you suspect objects may be hidden. \n\n1) FALSE \n\n2) TRUE  \n\n3) . \n\n4) .",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "On all UMS operated vessels and also on most other vessels the engine room is equipped with fire detectors. What requirements of testing and checking of the detectors are to be observed? \n\n1) Check the detector with heat and/or smoke (in accordance with instructions in its manual)\n\n2) All the mentioned alternatives. \n\n3) Check that the actual detector is giving appropriate signals to the central control unit and that all electric connections are in good order. \n\n4) When testing detectors by suitable A equipment ismoke and heat) check that the ensors self controlling system, e.g a flashing control light etc. is functioning",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "You are in open water and clear conditions. You are approaching the pilot station when you hear this signal from a vessel ahead of you. What does it signify? \n\n1) That the vessel is starting its engine and resuming its passage \n\n2) That the vessel is altering its course to starboard \n\n3) That the vessel is operating astern propulsion \n\n4) That the vessel is picking up its pilot",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "On area A3 the function "" Reception of shore to ship distress alerts is mainly based on: \n\n1) The use of VHF DSC and NAVTEX\n\n2) The use of MF DSC and INMARSAT C SAFETYNET \n\n3) The use of SARSAT COSPAS Epirbs  and NAVTEX \n\n4) The use of HF DSC and INMARSAT C SAFETYNET .",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "The PTT-switch must be: \n\n1) Pressed in during speaking  only to work semi-duplex \n\n2) Pressed to listen   \n\n3) Pressed in constantly to work simplex . \n\n4) Pressed in during speaking only to work duplex.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "During abandon ship exercise, what life-saving equipment must be demonstrated? \n\n1) Lifeboat radio \n\n2) Wearing and fastening of life-jackets and associated equipment  \n\n3) Location of immersion suits and thermal protective aids . \n\n4) How to communicate using the hand-held radios.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "What is the purpose of the O.D.M.E. (Oil Discharge Monitoring Equipment) printer? \n\n1) To prove fault conditions in the O.D.M.E \n\n2) None of the mentioned  \n\n3) To prove that oil has been pumped overboard according to regulations \n\n4) To prove that the O.D.M.E. system has been used.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "You have received the nine digit MMSI of a ship on your DSC equipment. In which publication will you find the name of the ship? \n\n1) The ITU List of Coast Stations \n\n2) The ITU List of Radio determination and Special Services  \n\n3) The ITU List of Ship Stations . \n\n4) The ITU List of Call signs and Numerical Identities of Stations used by the Maritime Mobile and Maritime Mobile-Satellite Services.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "As a minimum, how often shall life boats be launched with their assigned operating crew aboard and manoeuvred in the water according to SOLAS? \n\n1) Every three months. \n\n2) Every week. \n\n3) Every two weeks. \n\n4) Every month.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "The normal mode of operation for each coast station shall be indicated in: \n\n1) The ITU List of Call signs and numerical identities of station used by the maritime 3 mobile and maritime mobile-satellite services \n\n2) The ITU List of Coast Station  \n\n3) The ITU List of Radiodetermination and Special Services . \n\n4) The ITU List of Ship Stations.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "If all indications are that a cargo has been received without damages, irregularities or short shipment and the phrase (apparent good order and condition) is entered on the Bill of Lading, then this Bill is this said to be: \n\n1) A Bill of Lading completed for shipment. \n\n2) An endorsed Bill of Lading. \n\n3) Bill of Lading. \n4)A Due Title Bill of Lading.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "How many total frequencies are available for DSC distress alerting? \n\n1) Five (5)\n\n2) One (1) \n\n3) Two (2). \n\n4) Seven (7)",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Which of the statements best describes what happens to the sounding figures on an ECDIS chart display, when the safety depth figure is set? \n\n1) Figures less than the safety depth are highlighted in bold \n\n2) The whole sea area below that depth turns dark blue'  \n\n3) There will be alarms activated to let the operator know the depth under keel. \n\n4) The display looks the same as it did before and is unchanged.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "You wish to send a DSC-message because of a M.O.B. situation and assistance by other ships is required. You have to choose the category: \n\n1) Safety \n\n2) Distress \n\n3) Individual. \n\n4) Urgency.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "When using an ENC chart to passage planning, why should a scale at or near its compilation scale always be used? \n\n1) It is only at this scale that route validation is possible \n\n2) That is incorrect, as any ENC can be zoomed in or out for passage planning \n\n3) The chart detail is correct for its usage band \n\n4) It is only at this scale that a route can be plotted.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "On area A4 the function ""Transmission and reception of signals for locating"" is mainly based on: \n\n1) The use of MF DSC \n\n2) The use of SARSAT COSPAS Epirbs \n\n3) The use of HF DSC \n\n4) The use of SART transponders",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "The proper operation of an Inmarsat C-terminal can be tested by: \n\n1) Doing a ""link test"" \n\n2) Doing a ""recommissioning test"" \n\n3) Requesting a ""self test"" \n\n4) Sending a message to MF DSC.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "The operating mode of a pyrotechnic signal depends essentially on: \n\n1) The weather conditions of the moment \n\n2) Instructions or diagrams printed on its casing by the manufacturer \n\n3) A definite standard process  \n\n4) The fact that the user is on board a liferaft, a lifeboat of ship",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "You are a Senior Officer of the Watch on vessel ""A"" and are passing through the Straits of Gibraltar. The vessel's speed is 18 knots and your vessel is overtaking several other vessels, when the visibility reduces down to about 2 nm. What aspects would you consider when establishing a ""safe speed"" for your vessel? \n\n1) Safe speed should be where the vessel can come to a stop within the visible range  \n\n2) A safe speed is where a vessel can take proper and effective action to avoid collision and be stopped within an appropriate distance \n3) Deciding safe speed consider: 2 miles visibility; traffic density; manoeuvrability of vessel; effectiveness of navigational equipment (ARPA etc); state of sea and currents and navigational hazards.\n\n4) Adjust my track to follow Route 1 or 2  illustrated and reduce speed down to half speed, approximately 8 knots.",
                           "https://t.me/picturesforbo/100", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "The proper operation of an Inmarsat C- terminal can be tested by:  \n\n1) Sending a message to MF DSC \n\n2) Requesting a 'self test \n\n3) Doing a ""recommissioning test""  \n\n4) Doing a ""link test""",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "In relation to OPA 90, Which of the following statements is correct? \n\n1) COTP-zones may have additional rules and regulations \n\n2) OPA-90 specify all oil cargo related rules and regulations \n\n3) OPA-90 specify rules and regulations for all COTP-zones \n\n4) After implementation of OPA-90 there are no area specific rules and regulations",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "What mode must be used on the MF/HF transmissions when making a radiotelephone call: \n\n1  G3E \n\n2) J3E \n\n3) F1B/J2B \n\n4) H3E",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "What is the world-wide system operated by the US Coast Guard exclusively in support of search and rescue operations? \n\n1) The U.S. Command and Control Rescue (USCOMR) Service \n\n2) The Worldwide Maritime Mutual Assistance Programme (WMMAP) \n\n3) The Automated Mutual-Assistance Vessel Rescue (AMVER) System \n\n4) The International Search and Rescue Coordination System",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Who is responsible for the regular security inspections of the ship? \n\n1) The Company Security Officer \n\n2) The Port Facility Security Officer \n\n3) The Classification Society.  \n\n4) The Ship Security Officer",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "What colour flag is used to signal a safe landing place for small boats? \n\n1) Green  \n\n2) Blue \n\n3) White  \n\n4) Yellow",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Which statement(s) is true of a gasoline spill? \n\n1) It is not covered by the pollution law \n\n2) It is visible for a shorter time than a fuel oil spill \n\n3) It will sink more rapidly than crude oil  \n\n4) It does little harm to marine life",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "What percentage of the baggage is required to be checked at Security Level 1? \n\n1) 25-50% of the baggage is required to be checked at Security Level 1.  \n\n2) 5-15% of the baggage is required to be checked at Security Level 1. \n\n3) The percentage is not specified.  \n\n4) 100% of the baggage is required to be checked at Security Level 1",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "When a vessel violates the oil pollution laws, who may be held responsible? \n\n1) Officers only  \n\n2) Captain only \n\n3) Shipowners only  \n\n4) Any one involved in the operation.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "A SART is used by a sessel in distress. This SART is seen on the screen of a: \n\n1)3 Cm radar  \n\n2) Both 3 Cm and 10 Cm radar \n\n3)10 Cm radar  \n\n4) Special radar",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "If the speed on a vessel doubles, by approximately how much will the force from it rise? \n\n1) The force will be Doublet  \n\n2) The force will be Quadrupled \n\n3) The force will be Tripled \n\n4) The force will be Quintupled",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "What does the term DISCHARGE mean, as used in the Oil Pollution Regulations? \n\n1) Leaking \n\n2) Dumping \n\n3) All the other alternatives  \n\n4) Spilling",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "In open water, you see a collision between two other ships. What immediate action should you take? \n\n1) Slow down and standby to see if any assistance is required \n\n2) Send out a distress relay message \n\n3) Contact one or both vessels involved in the incident and offer assistance \n\n4) Nothing, proceed on passage unless they are in distress",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "By ""collect call"" is meant: \n\n1) A call for account of the receiver \n\n2) A group call \n\n3) An urgent call  \n\n4) A call to collect the charges in office",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "What is SOPEP?  \n\n1) A Ship-Owners Permitted Entry Plan \n\n2) A Shipboard Oil Pollution Emergency Plan \n\n3) A Seafarer's Offical Pension and Employment scheme  \n\n4) A Schipboard Oil Pollution Exemption Procedure",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Give the meaning of the following symbol \n\n1) Rocket parachute flares \n\n2) Survival craft distress pyrotechnic signals \n\n3) Line throwing appliance  \n\n4)  Lifeboat hand flare",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "What are the main advantages to the Navstar, Glonas and Galileo satellite navigation systems? \n\n1) They are all made specifically for ships and marine operations \n\n2) If a vessel uses any one of them, there is  no need to practice other forms of navigation \n\n3) Satellite navigation systems also give 2 information about weather and wave conditions \n\n4) These satellite systems give world-wide coverage 24 hours a day",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "It is important for hatch coaming compression bars to be maintained in good order on a General Cargo Vessel so that: \n\n1) Hatches can be properly sealed. \n\n2) There is no steel contact between the hatch covers and hatch coaming. \n\n3) Water can drain out from the hatch coaming drains. \n\n4) Hatch covers remain water tight.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "A distress-call received via RCC should: \n\n1) Always be given receipt \n\n2) Only be given receipt, if the master has confirmed that assistance indeed can be given \n\n3) Always be relayed  \n\n4) Be given receipt, even when indubitably too distant from the distress case",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "On a MF/HF-transmitter-receiver there is a volume control. Another name for this is: \n\n1) HF-gain \n\n2) Sensitivity \n\n3) LF-gain  \n\n4) RC-gain",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "A General Cargo vessel has a 50 tonne SWL heavy lift derrick and a load of 48 tonnes is to be loaded. The lifting gear of slings and spreader bar weighs 4 tonnes. In this case, it would be correct to state that: \n\n1) The load can be loaded because the SWL can sometimes be exceeded by small amounts in cargo operations, since the Breaking Load of the slings is much higher. \n\n2) The load cannot be loaded because the combined weight of the load and the lifting gear must be at least 10% less than the SWL of the derrick. \n\n3) The load can be loaded because the 2 load itself is less than the SWL of the derrick  \n\n4) The load cannot be loaded because the combined weight of the load and the lifting gear will exceed the SWL by two tonnes.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "The Master is responsible that all crew participate in monthly emergency drills. If 25% of the crew- or more has not participated in such drill during the last month, what is the time limit to conduct such a drill after the vessel has left a port? \n\n1) Within 24 hrs\n\n2) Within 12 hrs \n\n3) Within 48 hrs  \n\n4) Within 30 hrs",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "When a coastguard-station wants to send a gale-warning by DSC it will happen in the category: \n\n1) Security \n\n2) Safety \n\n3) Urgency  \n\n4) Routine",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Which organisation verifies the computational results and stored ship data used by the stability program loaded on a vessel's computer? \n\n1) The manufacturer. \n\n2) The master. \n\n3) The Classification Society. \n\n4) The engineer attending the installation and initial on-site testing.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "What is the purpose of the � SQUELCH � on a VHF transmitter/receiver? \n\n1) Switch to another channel \n\n2) Increase the sound signal of the receiver  \n\n3) Increase the range of the transmitter  \n\n4) Reduce the ""noise"" in the background",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "A battery of 24 Volt supplies during 10 hours a current of 6 ampere. What is the capacity supplied: \n\n1) 60 Ah \n\n2) 240 Ah  \n\n3) 48 Ah  \n\n4) 144 Ah",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "The log-in of an Inmarsat-C installation is important: \n\n1) To inform the LES, that one is available for messages offered \n\n2) To inform the NCS that one is available for messages offered  \n\n3) To inform the addressee, that one is available for messages offered  \n\n4) To keep watch on Sat-C for safety messages",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "A MMSI number consist of: \n\n1) 10 digits \n\n2) 6 digits  \n\n3) 9 digits \n\n4) The call sign followed by 4 digits",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "A satellite receives the transmissions of the 406 MHz Cospas-Sarsat EPIRB. The transmissions of the EPIRB will be: \n\n1) Exclusively passed on to a LUT if the satellite sees both the EPIRB and the LUT \n\n2) Passed when the satellite in passing the equator \n\n3) Exclusively passed on to a LUT only between 70 degrees N and 70 degrees S\n\n4) Always passed on to a LUT",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Where should the VHF survival craft transceivers be located during normal operation of the ship? \n\n1) On the bridge \n\n2) Near the liferaft \n\n3) In the lifeboats \n\n4) Near the gangway",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Who can contact the Designated Person with their safety concerns? \n\n1) The company's shore staff only \n\n2) All crewmembers  \n\n3) Senior officers only \n\n4) The Master only",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "As per the the IMDG Code, an ""article"" is referred to as: \n\n1) A form that contains important information about a hazardous substance. \n\n2) Something that is packed within a freight container. \n\n3) A device that contains a dangerous substance or mixture of substances. \n\n4) A device that is responsible for initiating a dangerous reaction.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "By FleetNET communication is understood: \n\n1) An urgent message for all ships in a particular area \n\n2) A HF-NBDP-message destined for ships in a certain geographical area  \n\n3) A MSI-message destined for ships in specific geographical area \n\n4) An EGC-message destined for ships with the same group call number",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "The value of GZ is no longer able to be calculated using GM Sine Angle of Heel formula at? \n\n1) Larger angles of heel. \n\n2) 5 degrees angle of Heel.  \n\n3) Small angles of heel. \n\n4) Less than 5 degrees angle of heel to the side of the heavy load.",
                           "https://t.me/picturesforbo/76", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "What do you understand by the term ""Risk Assessment"", and how would this be carried out on board? \n\n1) Identify the hazards and specify the personal protective equipment that would be required to complete the work \n\n2) Identify the hazards, quantify the risks, put control measures in place, monitor the work activity and review \n\n3) Requires a great deal of preparation and involves recording everything on paper \n\n4) States than when work has a degree of risk that the work is not carried out",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Searches are often triggered by: \n\n1) News stories of stowaways. \n\n2) The receipt of a shipment of damaged stores. \n\n3) An increase in security level by the Flag State. \n\n4) Lost baggage.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "If pollution takes place, what would you do immediately? \n\n1) Inform the manager. \n\n2) Inform the vessel's agent.  \n\n3) Start clean-up operations. \n\n4) Report to relevant authorities.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "What type of bomb search should you conduct to avoid panic when the credibility of the threat is in doubt and you don't want to disrupt ship business? \n\n1) Nominated officers search \n\n2) External search team \n\n3) Crew search \n\n4) Known hiding spot search",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "At present the MF/HF transmitter often has an automatic aerial turning unit. Should this fail: \n\n1) The transmitter will automatically keep operating on the MF and HF distress frequencies \n\n2) Its always possible to put the turning unit in a fixed position, so the MF distress frequencies can still be used  \n\n3) You can transmit but can not receive \n\n4) No distress frequencies can be used at all",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "A proper working of the 406 MHz Cospas- Sarsat EPIRB can be tested with: \n\n1) Regulation monthly test transmissions from RCC's \n\n2) Requesting RCC for the test  \n\n3) The testing function of the device \n\n4) Test transmissions from Cospas- Sarsat satellites",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "The carriage of logs on General Cargo vessels tends to cause: \n\n1) Spontaneous combustion. \n\n2) Increased levels of oxygen in the cargo holds.  \n\n3) Moisture absorption in the cargo holds. \n\n4) Oxygen depletion in the cargo holds.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "You are taking fuel on your vessel in the US when you notice oil on the water around your vessel. You are to stop taking fuel and: \n\n1) Notify the US Coast Guard \n\n2) Begin clean up operations  \n\n3) Leave the area \n\n4) Notify the Corps of Engineers",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "The reporting of incidents involving harmful substances and/or marine pollutants is regulated under: \n\n1) The UN Convention on the Reporting of 2 Accidents and Incidents which Present a Hazard to the Marine Environment 2004.\n\n2) Protocol I of MARPOL. \n\n3) Annex II to SOLAS 1974. \n\n4) Appendix B of the Supplement to the IMDO Code",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "According to Rule 26 of the International Regulations for Preventing Collisions and the illustrated lights, what type of vessels are they? \n\n1) These are two vessels engaged in fishing (pair trawling), showing the additional voluntary signals for shooting nets \n\n2) This is a vessel engaged in towing a disabled tow, restricted in its ability to manoeuvre, with a searchlight used to highlight the location of the tow  \n\n3) These are two vessels engaged in fishing (pair trawling), showing the additional volutary signals for hauling nets \n\n4) These are two vessels engaged in fishing.  using purse-seine gear. The searchlights are simply working lights",
                           "https://t.me/picturesforbo/77", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "You are on board a cargo ship. The ship is heavily listing to starboard, making impossible the launching of the survival craft stowed on this side. Lifeboats and liferafts are equally distributed on each side of the vessel. What should be the total number of persons that can be accommodated in the remaining survival craft stowed on the port side ? (*) N is the total number of persons that vessel is permitted to carry.\n\n1) at least 100 % N (lifeboat capacity: 50% N; liferaft capacity: 50% N) (*)\n\n2) at least 150% N (lifeboat capacity: 100% N; liferaft capacity: 50% N) (*) \n\n3) at least 150% N (lifeboat capacity: 50% N; liferaft capacity: 100% N) (*) \n\n4) at least 200% N (lifeboat capacity: 100 % N; liferaft capacity: 100% N) (*)",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "How often shall crew members participate in fire drills? \n\n1) Once every month \n\n2) Once every week  \n\n3) Once every year \n\n4) Once every 6 months",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "With an EPIRB: \n\n1) You must check the manufacturer of the battery \n\n2) You must check the date the battery must be replaced \n\n3) You must check if it is attached properly to a railing with the required line \n\n4) You must check the working of the charger and check the loaded condition of the battery",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Which of the following requirements regarding life-buoys correspond to present regulations? (SOLAS III/7.1) \n\n1) All the life-buoys shall be placed in  holders with quick-release arrangement\n\n2) At least one lifebuoy with self-activating 3 smoke shall be placed within the vicinity of the stern  \n\n3) Not less than half the total number of lifebuoys shall be provided with self- ignighting lights \n\n4) At least four life-buoys on each side of the ship shall be fitted with buoyant lifelines",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "At sea red rocket signals are seen. This is not reported by radio. You have to begin the distress alert procedure via VHF with the term: \n\n1) Distress alert \n\n2) MAYDAY RECU \n\n3) MAYDAY \n\n4) MAYDAY RELAY",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "On area Al the function "" Transmission of ship to shore distress alerts"" is mainly based on: \n\n1) The use of VHF DSC \n\n2) The use of HF DSC \n\n3) The use of SART transponders\n\n4) The use of portable VHF",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "The Muster List shall show the duties assigned to members of the crew. Which of the following duties shall be included according to present regulations? \n\n1) Preparation of immersion suits for passengers. \n\n2) Manning of fire parties assigned to deal with fires. \n\n3) Special duties assigned with respect to the use of pyrotechnics \n\n4) Operation of the vessel's propulsion system.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "The time indication 121310z means in maritime radio communication: \n\n1) 12th month, 13th day, 1000 hours UTC \n\n2) 12th day, 1310 hours local time \n\n3) 12th day, 1310 hours UTC \n\n4) 12th month, 13th day, 1000 hour Local time",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Which class of emission is used for ARQ NBDP transmissions?\n\n1) J3E \n\n2) G2B \n\n3) G3E \n\n4) FIB",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Who are responsible for safe working conditions onboard? \n\n1) Master, Chief Engineer & Chief Officer. \n\n2) The safety officer. \n\n3) The officer of the watch. \n\n4) The individual person.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "If the shipper wishes to ensure that a vessel or her operators will not be held responsible for any damage that may arise from the carrier issuing a clean Bill of Lading, even though the Mate's receipt is marked as ""unclean"", such a document is called the: \n\n1) A Letter of Credit. \n\n2) A Letter of Indemnity.\n\n3) An addendum to the Bill of Lading. \n\n4) An absolution clause in the shipping documents.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "In which of these circumstances can your ship request a DoS? \n\n1) Your ship has added a new port to its list  of ports of call.\n\n2) There is a heightened security risk for your ship and a port facility \n\n3) Your ship is conducting activities with a port or ship that is not required to implement an approved security plan.\n\n4) Your ship is operating at a lower security 4 level than the ship or port it is interfacing with.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "The frequency 121,5 MHz is used for: \n\n1) SART transponder \n\n2) INMARSAT E EPIRBS \n\n3) DSS VHF calls \n\n4) COSPAS-SARSAT EPIRBS",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "On board they want to make a DSC-call with a foreign coast-station. It is an urgent call. Preferably choose:: \n\n1) The national DSC-call frequecies of the coast-station concerned \n\n2) The international DSC-urgent frequency INMARSAT E EPIRBS \n\n3) The international DSC-urgent frequency \n\n4) The international DSC-call frequency",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "What type of dynamic forces may cause indent in plating on forecastle deck and main deck in way of pillars inside forecastle?: \n\n1) Impact pressure forces in way of abrupt or flared bow \n2) Pressure forces caused by green water on deck \n\n3) Slamming in way of flat bottom forward of light draught\n\n4) Forces created by waves on the forecastle",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "What is the minimum number of portable two way VHF walkie talkies for use in survival craft, that should be carried onboard vessels which comply with GMDSS regulations? \n\n1) 2 sets \n\n2) There is no requirement to carry them. \n\n3) 3 sets \n\n4) 1 set",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "To prevent overload of the MF/HF transmitter; \n\n1) Do not leave the transmitter on stand-by for too long, if not required \n\n2) Do not transmit too long at full power \n\n3) Switch over to low power intermitently\n\n4) Clean the dust filter of the fan regularly",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Give the meaning of the following symbol \n\n1) Rocket parachute flare \n\n2) Survival craft distress pyrotechnic signals\n\n3) EPIRB \n\n4) Survival craft portable radio",
                           "https://t.me/picturesforbo/74", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "If you use chemicals for cleaning up an oil- spill on the water, what would the chemicals do?  \n\n1) Remove the oil from the water \n\n2) Disperse or dissolve the oil into the water \n\n3) Contain the oil within a small area \n\n4) Absorb the oil for easy removal",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "A vessel has been in involved in a collision. Which procedure should happen immediately?  \n\n1) Communicate with the other ship \n\n2) Determine is there is any evidence of pollution \n\n3) There is assessment of the damage stability \n\n4) Determine any injuries of persons on board",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "When a satellite receives a ""distress alert"" from a Cospas-Sarsat EPIRB, the relay of the ""distress alert"" can be delayed because the satellite cannot immediately contact a: \n\n1) Coast station \n\n2) NCS before the satellite is actually seen by this ground station \n\n3) LES before the satellite is actually seen by this ground station \n\n4) LUT before the satellite is actually seen by this ground station",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Additional lashings on general cargoes must be considered when:  \n\n1) Heavy weather is anticipated for the planned voyage. \n\n2) Passing through the Summer Zone in winter months. \n\n3) After the vessel has started to encounter heavy weather conditions. \n\n4) Passing through the Tropical Zone in winter months.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Information about your ship's security arrangements and procedures is stored electronically. Which of these measures will help safeguard it from potential threats? \n\n1) Encoded email messages \n\n2) Passwords \n\n3) Protective markings \n\n4) Work history verification",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Which statement best describes how land moves, if at all, on an ECDIS set in North-up, relative-motion mode? \n\n1) The land is always in the middle of the screen \n\n2) This is a feature only seen on radar displays \n\n3) Land on the chart screen moves relative to the ship symbol \n\n4) Land is stopped with the vessel symbol moving across the sea floor",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "The transmitting receiving method, when both stations can transmit and receive at the same time is called:  \n\n1) Simplex \n\n2) Semi-duplex  \n\n3) None of the mentioned  \n\n4) Duplex",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "What is the main theme of modern safety practice? \n\n1) Making use of Risk Assessment as a means to improving safety \n\n2) Health & Safety at Work Act  \n\n3) Consult the chief officer before commencing work  \n\n4) Use the same practice that has been in place for some time",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "What is the emeggency frequency on M. F. (Medium frequency) radio?  \n\n1) 2617 Hz \n\n2) 2182 Hz  \n\n3) 7118 Hz  \n\n4) 1616 Hz",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "According to the International Labour Organisation, how often should lifting appliances and items of loose gear be thoroughly inspected by a competent person?  \n\n1) Biannually. \n\n2) Every 6 months.  \n\n3) Annually. \n\n4) Every 5 years.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "The relay of a distress-call by an RCC for coast-station begins with:  \n\n1) MAYDAY (3x) \n\n2) PAN PAN (3x)  \n\n3) Distress (3x) \n\n4) MAYDAY RELAY (3x)",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "One particular group of hazardous goods that is highlighted by the IMDG Code as potentially being the most dangerous for carriage is: \n\n1) Organic peroxides. \n\n2) Infectious substances.  \n\n3) Liquefied gases.  \n\n4) Toxic substances.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "An EPIRB has been activated accidentally. Which of the following is correct for cancelling the false distress alert?  \n\n1) Send a distress priority VHF DSC call and 2 make broadcast to all stations \n\n2) Call the nearest coast station and inform it that a false distress alert has been transmited  \n\n3) Make broadcast to all stations on VHF 16 \n\n4) Call a LUT and inform it",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "In a distress situation and immediately after the distress signal has been sounded, what is the next action to be taken by the Chief Officer on duty? \n\n1) Send distress signals to call for help \n\n2) Use the VHF-radio telephone to ask ships in the vicinity to stand by  \n\n3) Use the intercom to inform crew and passengers of the reason for the alarm \n\n4) Call the nearest coastal radio station",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "What has the most influence on the turning effect from an attached tug? \n\n1) Having a tug attached to the stern centre lead on a tug line \n\n2) Having a tug attached to the bow on a tug line \n\n3) Having a tug attached to a fairlead close to the pivot point (3x) \n\n4) The position of the applied tug force relative to the ship's pivot point",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Which of these measures would you implement to prevent drugs from being smuggled onboard your ship while it's berthed?  \n\n1) Maintain restricted areas. \n\n2) Eliminate fore and aft deck watch at night.  \n\n3) Search some of the packages, spares and stores received.\n\n4) Check a portion of the bags and packages brought onboard.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "As per SOLAS regulations, the general emergency alarm system must be tested. \n\n1) Every 3 weeks \n\n2) Every week \n\n3) Every month \n\n4) Every 2 weeks",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Is it necessary to be certified to be a lifeboat-commander? \n\n1) Yes, you must attend a one week course at a approved course center.  \n\n2) No  \n\n3) Yes, you must attend to a course held by certified personnel, and provide evidence of having maintained the required standards of competence every five years. \n\n4) No, the only thing you need is one hour instruction from a deck officer.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "For how is the health certificate valid for a seafarer above the age of  18?  \n\n1) No time limit \n\n2) Three month  \n\n3) One year  \n\n4) Two year.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "On a General Cargo vessel, a 16T derrick should be tested to a proof load of: \n\n1) 20T \n\n2) 18T  \n\n3) 24T \n\n4) 22T",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "MARPOL-Annex V. Disposal of garbage outside ""Special Areas"". After unpacking spares, you are left with a limited amount of packing materials. Is this prohibited, if not, what will be the nearest distance to land for disposal into the sea of these materials? \n\n1) 3 miles \n\n2) This is prohibited \n\n3) 12 miles \n\n4) 25 miles",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "The emergency battery of a GMDDS portophone:  \n\n1) Must be tested once a week \n\n2) Cannot be replaced  \n\n3) Must be replaced before the expiry date is exceeded \n\n4) Must be charged after expiry date",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "You are on a power-driven vessel underway in open water. You sight these lights on the port bow, on a steady bearing. The distance is closing. What are you looking at and what action will you take in compliance with the International Regulations for Preventing Collision at Sea? \n\n1) This is a power-driven vessel engaged in towing, more than 50 metres in length or less than 50 metres in length and showing a second masthead light, length of tow 200 metres or more, not under command. I will keep clear under rule 27 \n\n2) This is a power-driven vessel, more than 50 metres in length or less than 50 metres in length and showing a second masthead light, restricted in her ability to manoeuvre. The sidelight of a second vessel can be seen beyond her. Under rule 18, I am obliged to keep clear of the first vessel and will therefore take appropriate avoiding action \n\n3) This is a power-driven vessel engaged in towing, more than 50 metres in length or less than 50 metres in length and showing a second mast head light and the tow, the combined length of which is under 200 metres. The towing vessel is restricted in her ability to manoeuvre. I am seeing their starboard sides. The bearing is steady and risk of collision therefore exists. I will maintain my course and speed under rule 17 \n\n4) This is a power-driven vessel engaged in towing, less than 50 metres in length, length of tow under 200 metres and the tow, both being restricted in their ability to manoeuvre, seen from the starboard side. Under rule 18, I am required to keep clear and will take appropriate avoiding action.",
                           "https://t.me/picturesforbo/78", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Code signal concerning requests and general information on medical matters normally consist of: \n\n1) Letter M plus two other letters. \n\n2) Letter P plus two other letters.  \n\n3) Letter D plus two other letters. \n\n4) Letter H plus two other letters.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "When may a call for radio medical advice be precefef by the urgency-signal: \n\n1) Always \n\n2) In urgent cases  \n\n3) When you have on board  \n\n4) Never",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "What mode must be used on the MF/HF transmission, when transmitting a telex-message: \n\n1) G3E \n\n2) H3E \n\n3) FIB/J2B  \n\n4) J3E",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Where is the Safety Certificates for ships to be kept \n\n1) Posted up in a prominent place onboard the ship \n\n2) In the Captain's safe  \n\n3) Im the Owner's office  \n\n4) In the Captain's  office.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "What allowances should be applied to an echo sounder reading, to compare the depth of water with the depth shown on a chart? \n\n1) Position of transducer below the water surface and the height of tide \n\n2) A correction that should be applied to the charted depth value shown on the chart \n\n3) The distance between the pulse 3 Transmitter and Receiver, if different \n\n4) Shallow water effects causing ground interaction",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Messages sent via INMARSAT C are charged: \n\n1) On the number of kilobits of information 2 transmitted per block of 1024 bits \n\n2) On the number of kilobits of information transmitted per block of 256 bits \n\n3) On the basis of a six second minimum charge with six second incremental steps  \n\n4) On the basis of a three minute minimum charge with one minute incremental steps",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "How many maintenance must be provided by ships sailing in area A1 and A2 \n\n1) 3 \n\n2) 2 \n\n3) 1  \n\n4) 4",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "If one wants to transmit a weather report with an Inmarsat-C terminal one should use the following address: \n\n1) Sitrep \n\n2) OBS+ \n\n3) Meteorologocal Center   \n\n4) 41",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Where on the hull is the theoretical position of the hydrodynamic pivot point, when going astern and turning? \n\n1) Between 1/4 of the ship's length from the stern and the rudder post \n\n2) Amidships \n\n3) Between amidships and 1/4 of the vessel's length from the bow \n\n4) 1/3 of the vessel's length from the bow",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "A vessel is coming alongside a pier with two tugs assisting and there is little wind or current. How is it best to use the tugs? \n\n1) As shown in C, but only one tug made 2 fast forward for pulling and the other pushing aft \n\n2) As shown in 'A', pushing but also made fast to check the vessel's movement towards the berth with a pull off \n\n3) As shown in 'A, pushing on ship's side, but not made fast to allow the tug to move to another position if needed  \n\n4) As shown in 'B, made fast forward and  aft using the centre leads to enable the ship to be positioned",
                           "https://t.me/picturesforbo/79", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "The authority to order the use of distress signal or distress alerts is: \n\n1) Company safety officer \n\n2) The first person to discover the distress situation \n\n3) Only with the master \n\n4) The person designated to maintain communication duong distress situations",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "What does the term OIL mean, as used in the Oil Pollution Regulations? \n\n1) Sludge \n\n2) Fuel oil \n\n3) Oil refuse  \n\n4) All of the mentioned",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "With a davit launched lifeboat, what weight is required by SOLAS regulations to be used for the 5 yearly test of the davit and brake system? \n\n1) 1.1 times the total weight of the lifeboat when loaded with its full complement of persons and equipment. \n\n2) The equivalent to the total weight of the lifeboat when loaded with its full complement of persons and equipment. \n\n3) 0.8 times the total weight of the lifeboat when loaded with its full complement of persons, equipment and stores.  \n\n4) 1.25 times the total weight of the lifeboat when loaded with its full complement of persons and equipment.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "With maintenance of batteries it is of primary importance that: \n\n1) There is an absolute free access to the battery space \n\n2) The space where the batteries are stored is properly ventilated \n\n3) There is proper relative humidity in the space where the batteries are stored  \n\n4) The space is not oily",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "How is a vessel's navigational safety maintained when sailing between ports? \n\n1) Having the vessel guided by a VTS operation \n\n2) Only using traditional navigational techniques \n\n3) Having an effective passage plan followed by the bridge team \n\n4) Using an ECDIS as the main source of navigation",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "The IMO Convention that is not applicable to a general cargo vessel when it is carrying timber deck cargoes is: \n\n1) The International Convention on Load lines. \n\n2) MARPOL 73/78. \n\n3) SOLAS 74/78. \n\n4) The International Tonnage Convention.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "With an Inmarsat-C installation there is the addressing-option (special). Via this option: \n\n1) Give one of Inmarsat's (special access codes) \n\n2) You can deliver a message via a special telegram  \n\n3) You can send a message by express delivery \n\n4) You can plan a message to be delivered at a special time",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "What is the alcohol content in the blood permissible under US legistation before it is defined as intoxication?  \n\n1) 0.07% \n\n2) 0.04% \n\n3) 0.01%   \n\n4) 0.1%",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Which of the following statements is the most accurate in relation to the safety depth contour setting on an ECDIS? \n\n1) The safety depth contour value is best set at a high value \n\n2) The safety depth contour value is best set at a high value' \n\n3) The safety depth contour has to be set at a value to reflect the vessel's draught'  \n\n4) The safety depth safety depth contour value is best set at a low value",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "To maintain good relationship among the crew on board a vessel, one must be: \n\n1) Polite and diplomatic while talking to crew members \n\n2) Strict and authoritative while giving orders \n\n3) Give authority to others \n\n4) Understanding, Co-operative, and have respect from both sides.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Which one of the given requirements regarding survival craft muster and embarkation arrangements corresponds to the present SOLAS regulations? \n\n1) Muster and embarkation stations shall be readily accessible from accommondation and work areas.\n\n2) Muster and embarkation stations are to  be arranged separately to improve working conditions.  \n\n3) Searchlights to be provided at the launching station.\n\n4) Davit-launched survival craft muster and embarkation stations shall be arranged to enable stretchers to be placed in survival craft.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "What would be the preferred colour to use when maintaining the paint on shell, plating, structure and bottom/tanktopp in the engine room? \n\n1) The same colour as machinery and equipment. \n\n2) White or light grey to ensure all minor spills and leakages are noticed and dealt with. \n\n3) Dark brown/red colour to camuflage any minor leakages and oil spills. \n\n4) Whatever paint is available.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Once the Safety Management System is verified and working effectively, what document is issued to the ship? \n\n1) The Document of Compliance \n\n2) The I.S.M. Certificate \n\n3) The Safety Management Certificate\n\n4) The Document of Conformance",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Once the Safety Management System is verified and working effectively, what document is issued to the ship? \n\n1) The Document of Compliance \n\n2) The I.S.M. Certificate \n\n3) The Safety Management Certificate\n\n4) The Document of Conformance",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Your vessel has been involved in a collision and has developed a list. After sounding the general alarm and informing others of the situation, what other immediate steps should be taken? \n\n1) All of the options  \n\n2) Assess the compartments flooded to 2 determine the remaining stability \n\n3) Prepare for abandoning ship keeping all parties informed of the situation  \n\n4) Start discharging water using all available means. Monitor water ingress and any increase of draft or list to determine if the situation has stabilised.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Your vessel is close to the entrance of a port in thick fog. You hear the following signal. What does it mean? \n\n1) That the port is closed\n\n2) That there is a vessel at anchor in the vicinity. It is less than 100 metres in length  \n\n3) That there is a vessel at anchor in the vicinity. It is more than 100 metres in length \n\n4) That there is a vessel aground in the vicinity",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "On a ship involved in a collision, what should happen immediately after the accident has taken place?  \n\n1) The other ship should be contacted \n\n2) The bridge team should devise a plan of action \n\n3) Crew should follow an emergency procedure  \n\n4)  The master should be called",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "How often are ""abandon shop"" drills required to be held on cargo vessels according to SOLAS?  \n\n1) Once every year \n\n2) Once every 6 month  \n\n3) Once every week  \n\n4) Once every month",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "When a DSC-message of the 'distress category is received, in order to start distress alert communication in so far not indicated in the alert, you will switch to VHF channel:  \n\n1) 16  \n\n2) 85 \n\n3) 67  \n\n4) 13",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Which type of call will be sent by a ship sighting containers adrift in vicinity of her position? (No message about this problem was previously transmitted via NAVTEX or INMARSAT C SAFETYNET) \n\n1) Distress relay call \n\n2) Safety call \n\n3) Urgent call \n\n4) Distress call",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "The prescribed test of an approved portable VHF radio set (portophone) must be done once a: \n\n1) Quarter \n\n2) Year \n\n3) Month \n\n4) Week",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Which SOLAS certificate carried onboard has details of a vessel's bulkhead fire ratings? \n\n1) The Cargo Ship Safety Equipment Certificate. \n\n2) The MODU Safety Certificate. \n\n3) The Safety Management Certificate.  \n\n4) The Cargo Ship Safety Construction Certificate.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "When using an echo sounder in fresh water, the sounding indicated has a small error, what is the cause of this? \n\n1) The density of the water \n\n2) There should be no error with a properly working echo sounder \n\n3) The occurrence of weed and fish in fresh water \n\n4) The water temperature is probably higher",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "As per the IMDG Code, 'Proper Shipping Name' is defined as: \n\n1) The name under which a dangerous material, substance or article is described for export purposes in the country of loading. \n\n2) The name to be used in any documentation relating to the transportation of the dangerous substance, material or article, such as on forms, labels and placards.\n\n3) The name assigned by the manufacturer to a material, substance or article for the purposes of shipment. \n\n4) The correct chemical name of a potentially hazardous material, as identified from the Chemical Cargo List",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Which one of the listed requirements regarding the stowage of lifeboats and life-rafts corresponds to present SOLAS regulations? \n\n1) Davit-launched life-rafts shall be stowed on starboard side of the ship.\n\n2) Life-rafts shall be stowed close to the stern of the vessel \n\n3) Lifeboats shall be stowed attached to launching appliances.Month \n\n4) Life-rafts intended for throw-overboard 4 launching shall be stowed midships secured to means for transfer to either side.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Your vessel is progressing within a Traffic Separation Scheme and receives a navigational warning of another vessel progressing the wrong way within the scheme. What actions should be taken on the bridge, if any? \n\n1) Move into the inshore traffic zone \n\n2) Call the rogue vessel and point out its position. \n\n3) Slow down your vessel and proceed with caution, posting extra lookouts \n\n4) Proceed on passage and monitor the rogue vessel",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "According to the International Regulations for Preventing Collisions and the illustrated lights, what type of vessel is this and from what direction is it viewed? \n\n1) This is a vessel engaged in fishing other than trawling. making way through the water, with outlying gear extending more than 150m in the direction of the all- round white light, Looking of its port side \n\n2) This is a vessel engaged in fishing other than trawling, making way through the water, with outlying gear extending more than 150 metres in the direction of the all round red light. Looking at it from astern \n\n3) This is a vessel engaged in pilotage operations, deploying or recovering a pilot. Looking at its port side \n\n4) This is a vessel engaged in pilotage duties at anchor. Looking at its port side.",
                           "https://t.me/picturesforbo/80", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "A personal call means that: \n\n1) The applicant on board request the coast-station to personally guard the conversation with the shore subscriber \n\n2) The applicant on board wishes to have a conversation with a person whose name is known \n\n3) The applicant wants the call to be charged to some other person  \n\n4) The applicant on board request the coastal station to bring about a conversation with a shore subscriber by means of a scrambler",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "The safety message announces that a station:  \n\n1) Is in serious and imminent danger and needs immediate assistance \n\n2) Is going to be under repairs  \n\n3) Will relay a message concerning an important navigational or meteorological warning \n\n4) Has an very urgent message concerning the safety of a vessel, a plane or another means of conveyance",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "On a General Cargo ship which of the following statements is correct? \n\n1) Cold rolled steel coils may be loaded  \n\n2) Cold rolled steel coils are always shipped in stainless steel envelopes  \n\n3) Cold rolled steel coils may be loaded in rusty condition \n\n4) Cold rolled steel coils must never be loaded in rain",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "What is the minimum number of channels required for the portable two-way VHF's for survival craft?  \n\n1) Channels 6, 13 & 16 \n\n2) Channels 16 & 12  \n\n3) Channel 16 only  \n\n4) Channels 6, 12 & 16",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "A passage plan should indicate ways to fix position, and include which of the following methods? \n\n1) Radar ranges with parallel indexing  \n\n2) All of these suggested answers \n\n3) Visual navigation using land marks or celestial bodies  \n\n4) Position information from electronic systems",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "What is the purpose of the radiotelephony two tone alarm?  \n\n1) Attract the attention of the person on watch. \n\n2) Alert COSPAS/SARSAT satellites   \n\n3) Activate bridge watchkeeping receivers and attract the attention of the person on watch. \n\n4) Activate bridge watchkeeping receivers",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Is there any special area under MARPOL where it is forbidden to pump out any sludge or oil residues? \n\n1) There isn't any special area where it is  forbidden to pump out any sludge or oil residues \n\n2) There are 4 special areas: the Baltic Sea. Mediterranean Sea, Red Sea and Black Sea where it is forbidden to pump out any sludge or oil residues \n\n3) There are 3 special areas: the Baltic Sea, 2 Mediterranean Sea, and Black Sea where it is forbidden to pump out any sludge residues or oil \n\n4) There are special areas where it is forbidden to pump out any sludge or oil residues.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "By the degree of selectivity of a receiver is meant: \n\n1) Ability to make weak stations audible \n\n2) Ability to distinguish weak stations from adjacent stronger stations   \n\n3) Ability to receive all signals  \n\n4) Ability to prevent variations in the strength of radio frequency signal received",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "To inform ship of coast-stations messages, coast-stations give at fixed times: \n\n1) A list of the official identification numbers, for example the Maritime Mobile Service Indentity (MMSI). \n\n2) A traffic list with the call-sign of the ships involved in alphabetical numerical sequence  \n\n3) A list with the names of the ships involved spoken alphabetical numerical sequence. \n\n4) A list of all the messages for each vessel",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Which of the options best describes how a ""Balanced Rudder"" is constructed? \n\n1) The rudder has an additional flap attached to the trailing edge to improve rudder efficiency \n\n2) There is equal rudder area forward and aft 3 of the turning axis, the turning axis being at the geometrical centre of the rudder area  \n\n3) Part of the rudder area is forward of the turning axis, therefore reducing the load on the steering motor.  \n\n4) The rudder is operated by two steering  motors providing equal amounts of power to the rudder",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "For special category spaces on board general cargo ship, the minimum required air changes per hour should be:  \n\n1) 10 \n\n2) 20 \n\n3) 15  \n\n4) 6",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "The ship is navigating in dense fog where the visibility is less than one mile. The Arpa radar is set on a range 12 miles on a course of 314 degrees and own ship has a vector as shown. What is the vector mode selected on the Arpa? \n\n1) True vectors  \n\n2) Relative vectors. \n\n3) Relative vectors, ground stabilised  \n\n4) Relative vectors, sea stabilised",
                           "https://t.me/picturesforbo/81", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "With what system is a NAVTEX-message transmitted? \n\n1) ARG \n\n2) FEC \n\n3) URC  \n\n4) SELFEC",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "At what minimum height above sea level must a SART transponder be mounted? \n\n1) The proper function of a SART \n\n2) transponder doesn't depend on the height above sea level \n\n3) 1 metre  \n\n4) 0.5 metre",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Buoyant smoke signals shall be so designed as to burn or emit smoke: \n\n1) When under water \n\n2) Continuously after having been immersed for a period of 1 minute under Im of water \n\n3) Only when not in the water  \n\n4) Continuously after having been immersed for a period of 10 seconds under 100 mm of water when underwater",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Which radio frequency/channels are reserved for emergency communication? \n\n1) 2182 kHz/VHF channel 16 \n\n2) 2182 kHz/VHF channel 6 \n\n3) 2128 kHz/VHF channel 16 \n\n4) 2188 kHz/VHF channel 8",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "The IMO Cargo Stowage and Securing Code (CSS) indicates in the 'Rule of Thumb', the total strength of the lashings on each side of a heavy lift; what is the stated value ? \n\n1) The Maximum Securing load of the lashings must equal the 50% weight of the cargo unit. \n\n2) The Maximum Securing load of the lashings must equal the weight of the cargo unit. \n\n3) The Maximum Securing load of the lashings must equal twice the weight of the cargo unit. \n\n4) The Maximum Securing load of the lashings must equal five times the weight of the cargo unit.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "A Cargo Ship Construction Certificate has a validity of: \n\n1) 4 years\n\n2) 2 years \n\n3) 5 years \n\n4) 3 years",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "In making VHF communication or test transmission you must: \n\n1) Warn all ships in the vicinity \n\n2) First tap on the mike several times, but not more than 10 times \n\n3) With DSC use, first broadcast the carrier wave for at least three seconds\n\n4) Identify yourself with your call sign and/ or ship's name",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Whilst on passage, what type of position monitoring is conventionally considered to be the most suitable? \n\n1) One that employs more than one position fixing system \n\n2) A satellite system plotted on ECDIS or a paper chart \n\n3) Traditional forms of position fixing that are more trustworthy that satellite \n\n4) Gyro compass bearings from two lighthouses or fixed marks",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Which of the following is a Accounting Authority Identification Code? \n\n1) 227990850 \n\n2) FR01 \n\n3) F1B \n\n4) 2187.5",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Which equipment will detect a signal from a SART transpondder? \n\n1) DSC receiver \n\n2) Radio Direction Finder  \n\n3) X band radar \n\n4) S band radar",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "On area A4 the function (Transmission and reception of on scene communications) is mainly based on: \n\n1) the use of MF and/or HF R/T  \n\n2) the use of HF DSC  \n\n3) the use of SARSAT COSPAS Epirb \n\n4) the use of MF and/or VHF R/T",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "What is usually the effect on G when the ship is damaged with water ingress? \n\n1) It lowers \n\n2) It rises \n\n3) It first rises then lowers \n\n4) It is unchanged",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "For how long time must the printout from the Oil Discharge Monitoring Equipment (ODME) be retained onboard? \n\n1) Four years \n\n2) Three years \n\n3) Six months  \n\n4) Two yaers",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "What must be done if the Oil Discharge Monitoring Equipment (ODME) should fail during a ballast voyage? \n\n1) The failure must be repaired  \n\n2) The failure must be noted in the Oil Record Book  \n\n3) All of the mentioned must be performed \n\n4) If the failure cannot be repaired onboard, the ODME must be repaired before the ship commences its next voyage",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Which statement best describes how an ENC chart gives advice on sounding data quality? \n\n1) The chart has text on it that describes the sea floor type \n\n2) the chart has a Zone of Calculation function \n\n3) There are source data diagrams on the chart that can be read \n\n4) The chart has a Zone of Confidence function",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Which international organization is preparing conventions and rules for seafaring nations? \n\n1) International Maritime Organization (IMO) \n\n2) International Marine Association (IMA) \n\n3) International Labor Organization (ILO) \n\n4) International Ocean Safety Organization (IOSO)",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "The vessel is 20 miles off the coast and disabled because of engine failure, which will require at least 24 hours to repair. What initial actions should be taken to ensure the safety of the vessel? \n\n1) Contact the designated person ashore and request that a tug is arranged \n\n2) Steer away from danger until the vessel looses way, then if possible drop the anchor \n\n3) Display NUC lights and inform the nearest Coast Guard of you predicament \n\n4) Display NUC lights and send out a PAN warning on the hout using a VHF radio",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "You receive via the 8 MHz a DSC distress alert. The received DSC message is however distorted. The MMSI as well as the position are illegible. After listening at the 8 MHz telephone distress frequency, nothing is heard. This is because: \n\n1) You should have listened on VHF  \n\n2) First an acknowledgement of a coastguard station must be received via the 8MHz \n\n3) Telephone signals in the same frequency band are generally weaker than DSC signals \n\n4) You should have listened on the 2182 kHz",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "What factors cause a vessel to squat when it is moving through water? \n\n1) There is an increased effect of gravity due to closeness of the sea-bed \n\n2) There is a decrease in the water velocity and an increase of water pressure around the vessel's hull \n\n3) There is a positive pressure field created 2 ahead of the vessel and a negative one astern \n\n4) There is an increase in the water velocity and a decrease of water pressure around certain parts of the vessel's hull",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Hand flares and buoyant smoke signals can continue to burn or emit smoke after having been immersed for a period of 10s  \n\n1) Right if the immersion depth is smaller than 100 mm \n\n2) Wrong  \n\n3) Right if the immersion depth is more than 1 m \n\n4) Right",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "When conducting a risk assessment for a shipboard work activity, the two elements to be considered are: \n\n1) The available manpower and their 2 experience in this type of work.  \n\n2) The potential severity of harm and the likelihood that harm will occur.  \n\n3) The chance of an incident re-occurring and the potential effects of an loss. \n\n4) The time available to complete the task and the resources to hand",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "During the survey of Long Range Identification and Tracking (LRIT) equipment, which document must be available to the surveyor to demonstrate compliance with SOLAS? \n\n1) A report giving the result of the Performance Test, issued by the 2 manufacturer in compliance with the Flag State Authority requirements. \n\n2) A Statement of Installation and and  Testing by the Application Service Provider in compliance with SOLAS V/26-4. \n\n3) A report giving the result of the Conformance Test issued by an Application  Service Provider on behalf of an Administration \n\n4) The Certificate of Compliance with SOLAS V/19-1, bearing the serial number of the equipment installation.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "What is the colour and characteristic of a ""towing light"", as defined in the International Regulations for Preventing Collisions at Sea? \n\n1) One of two all-round amber, alternate flashing lights, displayed where they can best be seen  \n\n2) White, fixed, displayed as an additional light on the foremast over an arc of 225 degrees, from right ahead to 22.5 degrees abaft the beam on each side of the vessel  \n\n3) Amber, all-round, flashing, where it can best be seen \n\n4) Yellow, fixed, seen over an arc of 135 degrees and so arranged as to display 67.5 degrees from right aft on each side of the vessel",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Which of the following statements is correct with regard to IMDG Class 4 (flammable solids) cargoes loaded on a General Cargo vessel? \n\n1) The goods require protection against movement and can only be loaded if a cargo declaration is supplied by the shipper \n\n2) The goods can only be carried in the forward part of the vessel  \n\n3) The cargo is not covered by the requirements of the IMDG Code  \n\n4) The cargo can be stowed anywhere on the vessel",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "For a General Cargo ship not specifically designed for carriage of containers, the maximum stowage height for containers on deck is limited to: \n\n1) The height of the wheelhouse. \n\n2) One container high.  \n\n3) Two container high.  \n\n4) Three container high.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Which statement about the use of profiling onboard a ship is true? \n\n1) Profilers need at least half an hour to gather the information they need. \n\n2) Only visitors can be profiled.  \n\n3) A random selection process must be established. \n\n4) Detection equipment can be used in place of profiling.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "The word NAVTEX is spelled conform the international phonetic alphabet: \n\n1) November, Anna, Victor, Tango, Eduard, X-ray \n\n2) November, Apple, Victoria, Tango, Echo, X-mas  \n\n3) November, Able, Valencia, Tripoli, Echo, Xantippe \n\n4) November, Alfa, Victor, Tango, Echo, X-ray",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Do the bridge team have to create a passage plan for transiting a canal or river where there will be an authorised pilot onboard? \n\n1) A passage plan is always required, even with an authorised pilot \n\n2) A passage plan is required only when 2 there is no pilot on board   \n\n3) A passage plan is only required up to the destination pilot station \n\n4) A passage plan is required for all deep sea passages, but not for transiting a canal under pilotage",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "During a pre-loading survey on board a General Cargo ship, the most efficient method of testing the weather tightness of the hatch covers is considered to be: \n\n1) Chalk test. \n\n2) Ultra sonic test.   \n\n3) Visual inspection.. \n\n4) A Hose test.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Every inflatable liferaft, infatable lifejacket and hydrostatic release units shall be serviced: \n\n1) Every 18 month  \n\n2) Every 24 month  \n\n3) Every 12 month \n\n4) Every 36 month",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Which of the following prevention actions offers the guarantee of an efficient intervention in an emergency \n\n1) Training of the crew  \n\n2) Planning of the emergency \n\n3) The installation of protective measures \n\n4) All the listed answers",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "According to the International Regulations for Preventing Collisions and the illustrated lights, what type of vessel is it? \n\n1) This vessel is not under command, but is making way through the water \n\n2) This is a vessel constrained by her draft \n\n3) This vessel is not under command and stopped in the water  \n\n4) This vessel is aground",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "The emergency fire pump is in accordance with good seamanship and precautionary routines run and tested weekly. Routine checks and maintenance are normally carried out by dedicated personnel. To ensure safe and appropriate operation of the pump, would you consider it beneficial that the same dedicated personnel operate the pump in emergencies? \n\n1) Only senior engineers should operate the emergency pump.  \n\n2) In case of accidents, it is important that a wide range of personnel must be permitted and trained to operate the pump. \n\n3) To ensure safe operation of the emergency pump,only dedicated personnel must be permitted to operate the pump. \n\n4) Only senior deck officers should operate the emergency pump.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "What is the name of the reference manual, jointly produced by the International Maritime Organization and the International Civil Aviation Authority, which currently outlines the organization and management of search and rescue activities at sea? \n\n1) The Merchant Ship Search and Rescue (MERSAR) Manual \n\n2) The Internation Maritime Search and Rescue (IMARSAR) Manual \n\n3) The International Aeronautical and Maritime Search and Rescue (IAMSAR) Manual \n\n4) The Search and Rescue (IMOSAR) Manual",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "EGC is short for: \n\n1) Emergency general ship call  \n\n2) Exchange Geigraphic Call \n\n3) Exchange Group Call \n\n4) Enhanced Group Call",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "How often under SOLAS, is the performance test of a Voyage Data Recorder required by an approved testing or servicing facility? \n\n1) Annually.  \n\n2) When the data media is downloaded. \n\n3) At the Intermediate Safety Equipment Survey. \n\n4) When the battery is replaced",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "What is the meaning of the abbreviation (RQ) at the end of a DSC sequence? \n\n1) Problem of transmission  \n\n2) Acknowledgement request \n\n3) Acknowledgment broadcast \n\n4) End of sequence",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Your vessel is acting as the on scene commander during a distress rescue. Various vessels are interfering the distress traffic on the VHF. What message would you use to stop them interfering with this traffic? \n\n1) Seelonce securite  \n\n2) Seelonce distress \n\n3) Seelonce mayday \n\n4) Seelonce pan",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "A loaded General Cargo ship is bound from Brazil to Rotterdam during winter time. During the voyage, ventilation in cargo spaces should: \n\n1) Should occasionally be carried out as the  vessel is moving from a cold area to a warmer area.  \n\n2) Would only be carried out once, just before discharging the cargo. \n\n3) Should not be carried out as the vessel is moving from a cold area to a warmer area. \n\n4) Be carried out during voyage, as the vessel is moving from warm to colder areas.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Which action do you perform when you log in to a satellite ocean region? \n\n1) You inform the NCS that the SES is available for comunications.  \n\n2) You update the ship's position \n\n3) You select the CES through which you wish to send a message.\n\n4) You adjust the antenna.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "When a pilot is in attendance for navigation in a compulsory pilotage area, should the Master discuss the vessel's passage plan with them? \n\n1) No often there is not enough time and the pilot will be experienced  \n\n2) Yes-this is very much part of the Master/ Pilot information exchange \n\n3) No- because an authorised pilot does not need to be shown a passage plan \n\n4) Yes- as the pilot will not bring their own passage plan",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "When loading heavy lift cargoes on a general cargo vessel, positive stability can be maintained by: \n\n1) Monitoring the vessel's stability during  the loading operation and not allowing the vessel to list on the side of the load, \n\n2) Completely filling those double bottom tanks below the cargo hold where heavy cargo is being loaded. \n\n3) Completely filling the ship's double bottom tanks and continuously monitoring the loading operation.\n\n4) Listing the vessel to the opposite side to which the load is being lifted.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Which PPM is allowed for discharging of (Bilde Water) overboard? \n\n1) 0 PPM  \n\n2) 50 PPM \n\n3) 100PPM  \n\n4) 15 PPM",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Which of the following cargoes can normally be loaded next to each other in the same space of a General Cargo vessel? \n\n1) Drums of cement and steel pipes \n\n2) Drums of cement and bagged milk powder \n\n3) Rolls new carpets and drums lubricating oils \n\n4) Pallets of pesticides and bagged grain",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Distress MF communications should normally be operated: \n\n1) In J3E mode - on duplex basis \n\n2) In J3E mode on simplex basis \n\n3) In G3E made-on-duplex basis \n\n4) In G3E mode on simplex basis",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Which one of the listed requirements regarding life-saving appliances corresponds to present regulations? \n\n1) All prescribed life-saving appliances shall be fitted with the manufacturers name and Logo  \n\n2) All prescribed life-saving appliances shall have marking in red colour \n\n3) All prescribed life-saving appliances shall be made of non-combustible or fire retardant material \n\n4) All prescribed life-saving appliances shall be of such a colour that they are in contrast to the surrounding colour",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "You are proceeding along a coastal route when you hear this signal. The visibility is severely restricted. What does the signal mean? \n\n1) There is a vessel aground in the vicinity. She is less than 100 metres in length. She is sounding an additional warning to approaching vessels to navigate with extreme caution  \n\n2) There is a vessel at anchor in the vicinity. She is more than 100 metres in length. She is sounding an additional warning signal to approaching vessels, directing them to (keep clear) \n\n3) There is a vessel at anchor in the vicinity. She is less than 100 metres in length. She is sounding an additional warning to approaching vessels that they are running into danger \n\n4) There is a vessel aground in the vicinity. She is more than 100 metres in length. She is sounding an additional warning to approaching vessels that they are (running into danger)",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "The ship's lifting plant must be proof load tested and all parts thoroughly examined at intervals not exceeding: \n\n1) 5 years   \n\n2) 1 year  \n\n3) 3 years \n\n4) 6 months",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "The carriage of bagged Ammonium Nitrate in cargo holds of a General Cargo vessel is associated with: \n\n1) Build up of carbon dioxide gas \n\n2) Risk of explosion \n\n3) Corrosion of steelwork \n\n4) Spontaneous combustion",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "When a vessel berths with a beam current, what happens to the force exerted by the current if the underkeel clearance is very much reduced? \n\n1) It will remain unchanged because the 2 force is a function of the length of the vessel \n\n2) It reduces because the hull acts to block the flow of current \n\n3) It rises very considerably because of the shallow water under the hull \n\n4) It will remain unchanged because the force is a function of the current speed",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Information on the forces that may cause cargo shifting on a general cargo vessel may be available by referring to:\n\n1) The Code of Safe Practice for Solid Bulk Cargoes (BC Code)  \n\n2) The Cargo Securing Manual (CSM). \n\n3) The ship's stability manual.\n\n4) The Cargo Stowage and Security (CSS) Code",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Master of every ship must provide:\n\n1) A link between the shipboard training officer and the company training officer ashore \n\n2) Proper rest to the crew after each training programme \n\n3) the training during crews working hours only  \n\n4) Facilities to conduct training whenever required by the training officer",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "What does ISM stand for?\n\n1) International Ship Measurement and Pollution Control \n\n2) The International Management Code for the Safe Operation of Ships and for Pollution Prevention \n\n3) Internal Ship Safety Management \n\n4) International Safe Manning Certification",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Give the meaning of the following symbol? \n\n1) Parachute landing area \n\n2) Rocket parachute flares  \n\n3) Survival craft distress pyrotechnic signals \n\n4) Line throwing appliance",
                           "https://t.me/picturesforbo/82", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "The lifting plant on a General Cargo vessel be proof load tested: \n\n1) Every four years and after major repairs and modifications. \n\n2) Only when major repairs have been carried out to the equipment.  \n\n3) Only when major repairs have been carried out to the equipment. \n\n4) When equipment is new, every five years and after repairs or major modifications.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "The segregation requirements for Dangerous Goods to be loaded on a General Cargo ship may be obtained by referring to: \n\n1)The IMO International Maritime Dangerous Goods Code. \n\n2) The IMO Bulk cargo Code. \n\n3)  IMO SOLAS Handbook. \n\n4) The Cargo Securing manual",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "*Which one of the given requirements regarding manning and supervision of survival craft corresponds to the SOLAS regulation? \n\n1) Every motorised survival craft shall have a certificated engineer assigned \n\n2) A deck officer or certificated person shall be placed in charge of each survival craft to be used  \n\n3) There shall be at least 5 trained persons on board, mustering and assisting untrained persons\n\n4) Every lifeboat required to carry radio telegraph installation shall have a deck officer capable of operating the equipment assigned",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "The prescribed periodic tests of the radio set must be entered in: \n\n1) Ship's deck log. \n\n2) Equipment manual  \n\n3) Radio Log \n\n4) Manual maritime radio communication.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Which option best completes the following statement? 'The version of the IHO presentation library on the ECDIS is important because... \n\n1) ...it influences the colours on the display \n\n2) ...it is where the files for maintenance of the system software are stored  \n\n3) ..it allows ECDIS to decide on the scale setting of the chart\n\n4) ...if it is not the latest version, the ECDIS will not be compliant",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "At sea there is a container adrift which can be a danger for navigation. The call starts with: \n\n1) SECURITY (3x) \n\n2) MAYDAY (3x) \n\n3) URGENT (3x) \n\n4) PAN PAN (3x)",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "You have an important navigational or meteorological warning to transmit. What call should proceed this message when made on the radio telephone? \n\n1) Victor Victor (3 times)\n\n2) Security Security (3 times) \n\n3) Mayday Mayday (3 times \n\n4) Pan Pan (3 times)",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "A vessel is equipped for all sea areas. In the middle of the Indian Ocean the EGC- receiver appears out of order. Is it still possible to receive MSI-messages? \n\n1) Yes with VHF DSC \n\n2) NO \n\n3) Yes, with the MF/HF-radio telex \n\n4) Yes, with the MF/HF-DSC",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "The most important consideration when planning the lashing system for a particular sea route on a General Cargo Vessel is: \n\n1) The size and weight of general cargo items to be loaded \n\n2) The breaking strength of lashing materials.\n\n3) Encountering heavy weather. \n\n4) Transverse accelerations.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "As per the IMDG Code, 'Marine Pollutant' is defined as: \n\n1) A substance which is subject to the provisions of Annex III of MARPOL \n\n2) Any substance which is deemed hazardous to the marine environment.\n\n3) A substance which is subject to the 3 provisions of Chapter V of SOLAS 1974, as amended \n\n4) A substance which, because of its tendency to degrade in seafood, or because of its hazard potential to the aquatic environment is subject to the provisions of Annex I of MARPOL, as amended, and carried by sea accordingly.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Who is responsible for the vessel's radio station and mandatory radio routines? \n\n1) The owners. \n\n2) The master. \n\n3) The radio officer.  \n\n4) Statutory authorities.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "According to the International Labour Organisation, how often should lifting appliances be re-tested? \n\n1) Annually, \n\n2) 2 1/2 years. \n\n3) 5 years.  \n\n4) 2 years.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "If drugs or suspected drugs are found onboard your ship, follow the five C's. Confirm, Clear, Cordon, Control and: \n\n1) Change \n\n2) Cheer \n\n3) Chuck  \n\n4) Check",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Whilst sailing through a narrow coastal passage, an ECDIS alarm indicates that number 1 GPS HDOP value is outside set limits. What should happen on the bridge? \n\n1) The receiver should be checked and the vessel's position confirmed by other means \n\n2) The watchkeeper should call the master and then adjust the limit so that the alarm is removed \n\n3) Number 2 GPS should be selected as the primary receiver and the number 1 GPS switched off \n\n4) The ECDIS should be switched off as it will now be in DR mode and misleading to the bridge team",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "The best way to ensure you get the equipment you need is to: \n\n1) Buy the newest models. \n\n2) Determine your needs and do some research. \n\n3) Buy what everyone else is buying.  \n\n4) Buy the most expensive equipment on the market",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Which of the following would be considered pollution, when discharged overboard, under the US water pollution laws? \n\n1) Oil \n\n2) Hazardous substances \n\n3) All of the mentioned  \n\n4) Garbage",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "The number of frequencies on which a MF/ HF-DSC distress alert multi-frequency call attempt can be transmitted is: \n\n1) 2 \n\n2) 5 \n\n3) 3  \n\n4) 6",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "You wish to send an e-mail using the Inmarsat-C installation. The message has to be composed in:\n\n1) ASCII \n\n2) The 400 protocol \n\n3) X25  \n\n4) National language of the LES",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "On a General Cargo ship, the most likely cause of a hatch cover hydraulic system to deteriorate would be: \n\n1) Due to repeated hatch cover operations. \n\n2) Due to dust and cargo particles lodged around the piston seals. \n\n3) Due to ice accretion on piston jackets \n\n4) Due to hatch cover operations in high summer temperatures",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "You wish to carry out a test transmission on your radio equipment. What precautions should be taken if any? \n\n1) Listen out to ensure that no safety/ distress traffic is in progress. \n\n2) Test transmission should be kept to a minimum. \n\n3) All of the items in the other alternatives should be done.  \n\n4) Test transmission should be carried out on artificial aerials and/or reduced power.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "For how long time should a SART transponder be able to operate in the active mode? \n\n1) 24 hours \n\n2) 96 hours \n\n3) 6 hours \n\n4) 8 hours",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "What factors should influence the speed set on a vessel when connecting up a tug? \n\n1) The type of tug and its desired position on the vessel \n\n2) The type of tug and the size of its towline \n\n3) The location of the vessel and the type of fairleads that it has \n\n4) It is best to stop the vessel completely 4 before connecting, so there should be no speed",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "*As far as human factor is concerned, which of the following actions should be considered as an efficient one? \n\n1) To train the fire brigade \n\n2) All the listed answers \n\n3) To establish inner rules to perform work of a special risk \n\n4) To equip them with better communication systems",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "What type of vessel would show the illustrated lights? \n\n1) A sailing vessel, seen from astern, where the edges of her sidelights are both visible \n\n2) A sailing vessel, at anchor \n\n3) A sailing vessel less than 20 metres in length, displaying the optional combined lantern in lieu of standard sailing lights, seen head-on \n\n4) A sailing vessel of less than 10 metres in length, displaying the mandatory combined lantern inlieu of sailing lights, seen head-on",
                           "https://t.me/picturesforbo/83", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "For a General Cargo ship to load Dangerous Goods in packaged form, it must have on board a: \n\n1) SOLAS Safety Equipment Certificate. \n\n2) Document of Authorization for the carriage of bulk IMDG Cargoes. \n\n3) Safety Construction Certificate for 2 carriage of IMDG cargoes in packaged form. \n\n4) Document of Compliance for carriage of dangerous goods.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "If the speed of a vessel through the water is HALVED, how will this effect squat? \n\n1) The squat effect will be reduced to approximately a quarter of its original value \n\n2) The squat effect will also be halved \n\n3) There will be very little change to the effects of squat \n\n4) There will be a significant change in the reduction of underkeel clearance, but the amount varies from ship to ship",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "What immediate action should be taken if a ship unexpectedly runs aground and stops? \n\n1) Hoist two black balls \n\n2) Stop engine(s)  \n\n3) Ring full astern \n\n4) Sound the General Alarm",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Which of the following items shall be included in an (abandon ship)-drill? \n\n1) Checking the distress signal rockets and other distress signals \n\n2) Checking that all crew and passenger moral is high  \n\n3) Checking that passengers and crew are suitably dressed and lifejackets correctly donned \n\n4) Checking the lifeboat provisions and supplies",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Where should the placard you are shown be located, according to U.S. Coast Guard regulations? (Title 33-Navigation and Navigable waters, � 155.440) \n\n1) In a conspicuous place at the bilge and ballast pump control station \n\n2) In a conspicuous place in each machinery space \n\n3) In the wheelhouse \n\n4) Both in a conspicuous place in each machinery space and in a conspicuous place at the bilge and ballast pump control station",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Your vessel is not in distress and not taking part in a distress operation. How would you impose radio silence on vessels which are interfering the distress traffic? \n\n1) Seelonce Distress \n\n2) Seelonce Pan \n\n3) Seelonce Securite \n\n4) Seelonce Mayday",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Which option best describes what target fusion is on an ECDIS? \n\n1) When two adjacent AIS targets come together \n\n2) Bringing together a displayed radar return and AIS target \n\n3) The discrepancy between radar and AIS displayed positions  \n\n4) When a target's AIS signal has a large error on it",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "A five yearly thorough survey of cargo gear on a General Cargo vessel should be carried out by: \n\n1) The master. \n\n2) A marine surveyor appointed by the company, \n\n3) A classification society surveyor. \n\n4) A deck officer designated by the master.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "The first time you send a DSC distress alert via the HF-band, you prefer the? \n\n1) 22 MHz band \n\n2) 12 MHz band \n\n3) 16 MHz band \n\n4) 8 MHz band",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "A General Cargo vessel develops an angle of loll while loading a heavy item of deck cargo alongside the jetty. You should immediately: \n\n1) Stop cargo, reduce FSE in tanks, lower weights within vessel and fill small ballast tank on low side of vessel.\n\n2) Stop cargo, increase FSE in tanks, lower weights within vessel and fill small ballast tank on high side of vessel. \n\n3) Stop cargo, increase FSE in tanks, lower weights within vessel and empty small ballast tank on low side of vessel. \n\n4) Stop cargo, reduce FSE in tanks, lower weights within vessel and fill small ballast tank on high side of vessel.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Why is it important to have good relationship on-board a vessel? \n\n1) Crew comes to know each 3 others problems \n\n2) It leads to better work performance and positive atmosphere among the crew \n\n3) It encourages crew to extend their contract \n\n4) It will prevent accidents from happening",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Non distress calls on 2182 kHz and VHF channel 16 should not exceed: \n\n1) Three minutes. \n\n2) Five minutes. \n\n3) One minute.\n\n4) Two minutes.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "The steps of the embarkation ladder used must be proportioned as it follows: \n\n1) length = 280 mm, breadth = 85 mm, depth-10 mm \n\n2) length = 380 mm, breadth = 145 mm, depth 20 mm \n\n3) length = 580 mm, breadth = 165 mm, depth 30 mm \n\n4) length = 480 mm, breadth = 115 mm, depth = 25 mm",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "By the term (Stand by) the operator of a coast-station means that one should: \n\n1) Wait until the coast-station calls again \n\n2) Switch back to the calling channel \n\n3) Give the position of the ship \n\n4) Wait on this channel for one hour",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "A greater number of lashings may generally be required to secure cargo forward on deck compared with amidships under deck of a General Cargo Vessel, because: \n\n1) The roll period is greater forward. \n\n2) The dynamic stresses on the lashing are much greater in the forward areas of the vessel. \n\n3) Heavier cargo is generally stowed forward.  \n\n4) The forward of the vessel is subjected to more rolling conditions.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "What are the conditions that influence the efforts for organising the fire fighting? \n\n1) Where the fire break out, the ships mobility, distance to the fire station and the size of the fire brigade \n\n2) Distance to the fire station and the size of the fire brigade, what is burning. possibility to get water \n\n3) Where the fire breaks out, how many fire teams are available, the strength of the fire, the ships mobility, what is burning and communication \n\n4) Where the fire break out, how many fire teams are available, what is burning. distance to the fire station",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "What is full form of VRP (OPA-90) \n\n1) Vessel Reporting Procedures \n\n2) Vessel Report Plan \n\n3) Vessel Response Procurement \n\n4) Vessel Response Plan",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Who is responsible for the development of the Ship Security Plan? \n\n1) The Company Security Officer \n\n2) The Port Facility Security Officer \n\n3) The Classification Society. \n\n4) The Ship Security Officer",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "When a character in the NAVTEX message sent is not received in the proper way: \n\n1) the message will not be printed at all until, with repeated transmission, it can be automatically compared and corrected \n\n2) Nothing or a special character will be printed \n\n3) Any other character will be printed \n\n4) A closely resembling character will be printed",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "The muster list shall show the duties assigned to the different members of the crew. Which of the given duties necessarily have to be included in the muster list? \n\n1) Clearing escape routes  \n\n2) Type of fires that can be encountered on board \n\n3) Preparation and launching of survival crafts \n\n4) Preparation and starting of emergency generator",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "With respect to the ISM, what training in addition to lifeboat and fire drills must be carried out? \n\n1) The boat drill and fire drill should be adequate to meet your needs  \n\n2) Mooring operations \n\n3) Bridge Team Management \n\n4) Familiarization, and other drills identified as necessary by the ship",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "You are onboard a vessel off the West African coast. You want to dump a mixture of food waste, glass bottles and floating packing materials. Is this allowed? and if so, how far off the coast would you have to be? \n\n1) This is prohibited  \n\n2) 3 nautical miles off the coast \n\n3) 25 nautical miles off the coast\n\n4) 12 nautical miles off the coast",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "How often should the lifeboat wire falls be turned and renewed? \n\n1) Renewed every three years  \n\n2) Turned at intervals of not more than 30 months and renewed every 5 years \n\n3) Turned every 30 months and needs only \n\n4)  to be renewed if the wire is in poor condition",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "When hot rolled steel coils are loaded on General Cargo ships, it may be correct to state that: \n\n1) They must always be shipped in stainless steel envelopes. \n\n2) They can be loaded in heavy rain  \n\n3) They must not be exposed to salt water contamination.\n\n4) They must always be loaded wrapped in water-proof plastic sheet.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "On area A4 the function (Transmission of ship to shore distress alerts) is mainly based on: \n\n1) The use of MF DSC and INMARSAT Epirbs \n\n2) The use of HF DSC and INMARSAT Epirbs \n\n3) The use of VHF DSC and VHF Epirbs\n\n4) The use of HF DSC and COSPAS SARSAT Epirbs",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "The majority of convensions adopted under the auspices of IMO fall into which of the three main categories: \n\n1) Maritime Safety, Prevention of Marine pollution, Liability and compensation  \n\n2) There are no conentions that fall under IMO \n\n3) Maritime Safety, STCW, Maritime Security \n\n4) Safety, Terrorism, ILO",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Your vessel is involved in a collision with another vessel. What should you as Master tell the Master on the other vessel? \n\n1) There should be no communication with the other vessel \n\n2) Name of vessel; IMO number; Port of registry; Port of destination of your vessel \n\n3) Explain your actions prior to the collision and request details of actions taken by the other vessel which resulted in the collision \n\n4) That their actions were totally wrong and it is their fault",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "When planning to cross an ocean, is it always best to use great circle sailing? \n\n1) Yes - because it is the easiest sailing to compute and then follow  \n\n2) Yes because an ECDIS in track control will do the computation and steer the route \n\n3) No-because there could be environmental or regulatory restrictions \n\n4) No because a Mercator course is more efficient, less distance and easier to follow",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "On board they want to have a dial-phone call via Inmarsat with the Apollogracht. In the guides the following ID's are found for the Apollogracht:344320000, 424432010, 424432020, 1300210, 36715. What ID should be chosen: \n\n1) 4424432010 \n\n2) 3424432020 \n\n3) 344320000 \n\n4) 1300210",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "During cargo watch on a General Cargo ship, if the OOW informs you that the condition of the discharge equipment such as slings and shackles being used by the stevedores is unsuitable for use, you should: \n\n1) Inform stevedores of concern and protest by letter. \n\n2) Continue discharge as planned and inform Designated Person Ashore (DPA). \n\n3) Provide ships equipment to discharge \n\n4) Refuse to discharge and inform the local agents.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "A general cargo vessel is loading to its Summer Marks. Upon completion of loading, the final level of the water would be at: \n\n1) The mid point between the summer and the tropical mark. \n\n2) The top of the summer load line mark. \n\n3) The top of the winter mark. \n\n4) The bottom of the summer load line mark",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "What is the probable cause of an error in the position shown on a GPS receiver set into '2D' fixing? \n\n1) The limit set on the HDOP figure is too great \n\n2)  the limit set on the VDOP figure is too small \n\n3) Incorrect height of the antenna set into the receiver \n\n4) The receiver has defaulted to 3D fixing and there is no overhead suleinte",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "This vessel is encountered at the mouth of a river. According to the International Regulations for Preventing Collisions and the illustrated shapes, what type of vessel is it? \n\n1) This is a vessel engaged in mine-clearance opetrations. The two balls in a vertical line indicate that it has a sweep mechanism deployed; the two diamonds in a vertical line indicate that the vessel should be given a clearance of at least 300 metres; the ball/diamond/ ball indicate that the vessel is restricted in her ability to manoeuvre \n\n2) This is a vessel engaged on port security duties. The two balls in a vertical line indicate that the port is closed; the two diamonds in a vertical line indicate that the port is engaged in mine- clearance operations; the ball / diamond / ball in a vertical line indicate that the vessel is restricted in her ability to manoeuvre \n\n3) This is a vessel engaged in dredging or underwater operations. The two balls in a vertical line indicate the side on which it is safe to pass; the two diamonds in a vertical line indicate the side on which an obstruction exists; the ball / diamond/ball indicate that the vessel is restricted in her ability to manoeuvre \n\n4) This is a vessel engaged in dredging or underwater operations. The two balls in a vertical line indicate the side on which an obstruction exists; the two diamonds in a vertical line indicate the side on which it is safe to pass; the ball / diamond//ball in a vertical line indiacte that the vessel is restricted in her ability to manoeuvre",
                           "https://t.me/picturesforbo/101", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "If a master initially responds to a distress but then, in special circumstances, decides not to proceed, who must they tell? \n\n1) Inform the Search and Rescue Mission Coordinator (SMC) of their decision and enter the reason in the vessel's logbook \n\n2) Inform the vessel owners of their decision and resume passage at the earliest opportunity \n\n3) Contact all the other units in the SARQU operation informing them of the decision to break off \n\n4) possible, inform the casualty of their If possib decision and communicate the reason",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "In what format will an On-Scene Co- ordinator report such information as on- scene weather and operation progress to other parties? \n\n1) POSREP \n\n2) SITREP \n\n3)SARREP \n\n4) OSCREP",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Your watchkeeper has just informed you that the vessel has collided with a sailing vessel. What action should be taken? \n\n1) Call the company, explain the situation and ask for instructions \n\n2) Tell the watchkeeper to sort out the problem \n\n3) Alarm the rescue centre and commence searching for survivors \n\n4) Tell the watchkeeper to proceed on passage",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Door to door shipment is covered under:\n\n1) A Multi-Phase Bill of Lading. \n\n2) An Ocean Bill of Lading. \n\n3) A Destination Bill of Lading.\n\n4) Through Bill of Lading",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "On board they want to send a safety-call to other vessels. The DSC safety-call:\n\n1) Has to contain a work-frequency \n\n2) May not contain a work-frequency \n\n3) May contain a work-frequency \n\n4) Will automatically send the correct working frequency",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "The International Convention for the Safety of Life at Sea (SOLAS) regulations, Chapter 5, deals with the Safety of Navigation and applies to which vessels? \n\n1) To vessels over a certain size \n\n2) To all vessels and all voyages with exceptions \n\n3) To ALL vessels that go to sea.\n\n4) To vessels with deadweight over 10 GOO tons",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "The display of a radiotelephone-installation shows the following selections: Transmitting mode: H3E Transmitting frequency: 2187,5 kHz The transmitting mode indicator is (flashing). This can mean that: \n\n1) The (H3E) mode is to be selected before transmitting on the 2187,5 kHz band \n\n2) You are ready to press the send buuton \n\n3) The transmitting mode is not compatible with the chosen frequency \n\n4) The radiotelephone-alarm signal must be transmitted now",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "On what wave band does the search and rescue radar transponder operate? \n\n1)6 GHz \n\n2) 2182kHz \n\n3) 8 GHz \n\n4)9 GHz",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "In the situation illustrated, what should be the power distribution of the tugs to maintain the ship sideways motion with only minor changes in the ship's heading? \n\n1) Considerably more power on the aft tug than the forward tug, while monitoring the ship's gyro heading \n\n2) Considerably more power on the forward tug than the after tug, while monitoring the ship's gyro heading  \n\n3) Full power on the forward tug and the after tug ceases to push, but continuously monitor the ship's gyro heading \n\n4) 9 Equal power on both tugs while monitoring the ships gyro heading",
                           "https://t.me/picturesforbo/84", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "On area A2 the function  (Transmission of ship to shore distress alerts) is mainly based on: \n\n1) The use of INMARSAT Epirbs \n\n2) The use of MF DSC \n\n3)  The use of SARSAT COSPAS Epirbs \n\n4) The use of VHF DSC",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "A dynamic test of the winch brake with a proof load equal to 1.1 times the weight of the survival craft or rescue boat and its full complement of persons and equipment should be carried out \n\n1) every three years \n\n2) every ten years \n\n3) every five years  \n\n4) every year",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Where would you find the document relating to the (Condition of Freeboard Assignment) onboard? \n\n1) With the Structural Survey File. \n\n2) With the Classification Records.\n\n3) With the Safety Construction Certificate.\n\n4) With the Loadline Certificate.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "As per the IMDG Code, 'Marine Pollutant' is defined as:\n\n1) A substance which is subject to the provisions of Annex III of MARPOL.\n\n2) A substance which is subject to the provisions of Chapter V of SOLAS 1974, as amended. \n\n3) A substance which, because of its tendency to degrade in seafood, or because of its hazard potential to the aquatic environment is subject to the provisions of Annex I of MARPOL, as amended, and comed by sea accordingly  \n\n4) Any substance which is deemed hazardous to the marine environment",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "The main purpose of a hatch cover ventilator grill on a General Cargo vessel is: \n\n1) To prevent moisture from entering the hold.\n\n2) To prevent sparks entering the cargo hold. \n\n3) To act as a strength member inside the ventilation shaft.  \n\n4) To prevent the ventilator fans from damage",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "What is usually the effect on G when the ship is damaged below the waterline, with water ingress? \n\n1) It rises \n\n2)  It is unchanged \n\n3) It lowers \n\n4) It first rises then lowers",
                           "https://t.me/picturesforbo/76", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "For how long time should a VHF survival craft transceiver be able to operate on its batteries? \n\n1) 24 hours \n\n2) 6 hours \n\n3) 12 hours \n\n4) 8 hours",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "The aerial system of an Inmarsat-C terminal consist of: \n\n1) An omni-directional aerial \n\n2) A rod aerial \n\n3) A flexible wire aerial \n\n4) A dish aerial",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Dish aerials used with \n\n1) None of the mentioned \n\n2) Inmarsat - B and - M \n\n3) Inmarsat-C and-M \n\n4) Inmarsat-A and-C",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "What is the result of an (unusually large metacentric height)? \n\n1) The vessel will have a great bending moment \n\n2) The vessel's tweendeck heights is too high \n\n3) The vessel will roll violently  \n\n4) The vessel will roll slowly or be unstable",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "A hand flare must have a burning period of at least: \n\n1) 10 Min \n\n2) 30 Sec \n\n3) 8Min  \n\n4)1 Min",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "On area A3 the function (Transmission and reception of on scene communications) is mainly based on: \n\n1) The use of HF/MF and/or VHF R/T and/or INMARSAT C \n\n2) The use of HF DSC \n\n3) The use of MF and/or HF R/T  \n\n4) The use of DSC and/or INMARSAT C",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "What is the result of a (high metacentric height)?\n\n1) The vessel's tweendeck heights is too high? \n\n2) The vessel will roll violently? \n\n3) The vessel will roll slowly or be unstable? \n\n4) The vessel will have a great bending moment?",
                           "https://t.me/picturesforbo/76", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "In area A1 the function (Transmission and reception of signals for locating) is mainly based on: \n\n1)the use of INMARSAT Epirbs \n\n2) the use of SARSAT COSPAS Epirbs \n\n3) the use of SART transponders \n\n4) the use of VHF DSC",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "The value of the GZ lever at small angles of heel on a General Cargo Vessel can be denoted by the formula: \n\n1) KN- Corrected KG x Sin angle of heel \n\n2) KN-KG x Sin angle of list. \n\n3) KM-Corrected KG x Sin angle of list. \n\n4) KM-KG x Sin angle of heel.",
                           "https://t.me/picturesforbo/76", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "From the list below, which is among the recommended actions for a vessel to take, on entering an area known for pirate activity? \n\n1) To transit with maximum safe speed \n\n2) To transit at night time only\n\n3) To confine all ship's personnel to one room onboard \n\n4) To turn off all lights",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Prior to loading general cargo on a General Cargo vessel, with regard to lashing wires, terminations, shackles, turnbuckles, pad eyes and D rings etc., you must make sure that: \n\n1) Lashing wires must be new whereas other accessories may be certified. \n\n2) They must all be certified and be visually inspected for any apparent damage. \n\n3) They must all be certified. \n\n4) They must all be visually inspected.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "When moving into an Emission Control Area for Sulphur, which of these is most important? \n\n1) That the change-over to low Sulphur fuel was started before entry into the ECA \n\n2) That the change-over to low Sulphur fuel is complete before arrival in port \n\n3) That low Sulphur fuel is actually being burned before entry into the ECA  \n\n4) That the change-over to low Sulphur fuel is started before arrival in port",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "According to the International Regulations for Preventing Collisions, these displayed lights indicate that this is one of two types of vessel. What are the two options? \n\n1) A vessel engaged on pilotage duty, engaged in deploying or recovering a pilot, seen head-on or a power-driven vessel underway, Imore than 50 metres in length or less than 50 metres in length and showing the second masthead light, seen head-on \n\n2) A power-driven vessel engaged in towing, more than 50 metres in length, or less than 50 metres in length and showing a second masthead light, length of tow under 200 metres, seen head-on OR a power-driven vessel underway. Less than 50 metres in length and displaying the second all-round white masthead light, seen head-on \n\n3) A vessel engaged in fishing, restricted in her ability to manoeuvre, shooting nets OR a vessel engaged in towing, less than 50 metres in length, length of tow under 200 metres, towing vessel restricted in her ability to manoeuvre, seen head-on  \n\n4) A power-driven vessel engaged in towing, less than 50 metres in length, length of tow under 200 metres, towing vessel and tow restricted in their ability to manoeuvre, seen head-on OR a power-driven vessel underway, more than 50 metres in length, or less than 50 metres in length and showing a second masthead light, restricted in her ability to manoeuvre, seen head-on",
                           "https://t.me/picturesforbo/104", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "An Inmarsat-C terminal is suitable for:\n\n1) E-mail, SMS, telex, chart and weather updates.\n\n2) Telephony, fax and data \n\n3) Telex only  \n\n4) Telephony, telex, fax and data",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "During an audit, adherence to the company cargo handling procedures can best be demonstrated: \n\n1) By providing a summary of out-turn figures for the auditor. \n\n2) By being able to provide comprehensive and verifiable documentary records of cargo operations.\n\n3) By requesting that an audit takes place during cargo operations \n\n4) By providing a summary of incident and A lost time figures for the auditor that reflects G SUCCUS and trouble-free system board.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Where several rescue units are engaged in a search and rescue operation, one of them may be designated as the On-Scene Coordinator (OSC). Which of the following descibes how this appointment will be made? :\n\n1) The coastguard will appoint the OSC using their vessel database to assess suitability \n\n2) The role of OSC is only taken by a naval ship close to the area \n\n3) The OSC will always be designated by the Search and Rescue Mission Coordinator \n\n4) An aircraft is usually appointed as the 4 OSC because of their speed",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "The ship-shore HF-telephone-channel 2228 consists of the frequencies 22081.0 kHz and 22777.0 kHz. In case of manual operation, one should tune the receiver on: \n\n1) 22081,0 KHz \n\n2) The common receiving frequency for the 22 mHz band \n\n3) 2228 KHz \n\n4) 22777.0 KHz",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "The DSC-controller displays the following: DOO: 246321000 CH16; S distress flooding After receiving this DSC message nothing more is received. Sending receipt on channel 16 does not give any response. One should first: \n\n1) Send a DSC distress alert relay \n\n2) Send a DSC acknowledgement \n\n3) Listen out on VHF-channel 67 \n\n4) Inform the safety officer",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "If for some reason a vessel does not comply with a Classification Society's requirements, what can a surveyor issue to the vessel enabling it to sail to the next port or for a period of time? \n\n1) A Notification of Deficiency. \n\n2) A Condition of Class. \n\n3) A Notification of Detention. \n\n4) A revised Class Notation.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "The display of the DSC-controller on board is showing the following lines: TX call:Selectiveto: 02114200 Category: RoutineUSB:telephony DSC Tx 2189.5 kHzsave>send< This DSC- message must be transmitted in the mode: \n\n1) This cargo can only be loaded under deck \n\n2) Cargo of this type can be loaded anywhere on board the vessel \n\n3) This cargo can only be loaded on deck \n\n4) Cargo must be loaded in a protected location and preferably under deck if IMDG Code allows",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Which of the following statements is correct with respect to IMDG cargo, loaded on a General cargo vessel, that is also classed as a Marine Pollutant \n\n1) J3E \n\n2) G3E \n\n3) FIB \n\n4) H3E",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "That the 406 MHz Cospas-Sarsat EPIRB is in proper working order can be tested with: \n\n1) The testing function of the device \n\n2) Regulation monthly test transmissions from RCC's \n\n3) Requesting RCC for the test \n\n4) Test transmissions from Cospas- Sarsat satellites",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "To receive distress alerting and MSI via an Inmarsat-C set vessels must have: \n\n1) A radio officer on board \n\n2) SES or an EGC receiver \n\n3) Suitable for 518 kHz NAVTEX receiver \n\n4) MF/HF radio telex scanner with printer",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "The DSC-controller display the following: DOO: 244562000 CH16; S distress sinking After receiving this DSC message the following is done immediately: \n\n1) Give a (DSC-acknowledgement)\n\n2) Call the Chief officer \n\n3) Listen out on VHF channel 16 \n\n4) Send a distress alert relay",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Which option best describes how an operator establishes what an isolated danger symbol represents, when seen on the chart display of an ECDIS? \n\n1) Check the surrounding area for any clues on the sea floor \n\n2) Check the chart symbols catalogue to ascertain the meaning  \n\n3) Check with a senior officer \n\n4) Interrogate it and ask for a pick or information report",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Onboard the following message is received on the DSC controller: DOO: 245329000 CH16; S distress ack 244123000 What station sent the distress acknowledgement? \n\n1) 245329000 \n\n2) None of the given  \n\n3) 3002453290 \n\n4) 244123000",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Steel coils when loaded on a General Cargo ship tend to be subjected to: \n\n1) Tearing. \n\n2) Crushing and distortion. \n\n3) Bending. \n\n4) Chemical reactions between the steel banding and outer envelope.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Which of the following requirements regarding on board stability data corresponds to present regulations? (NSCL 4/12.1) \n\n1) A calculation example showing use of (GM) limitation curves. \n\n2) Drawings and caculations documenting the stability of the ship, both in intact and all possible damage condition. \n\n3) A calculation example showing the use of (KG) limitation curves \n\n4) Stability data produced by stability calculation instruments..",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Prior to loading cotton on a General Cargo vessel, it is important to ensure that: \n\n1) The cargo hold ventilation system is thoroughly examined. \n\n2) Tank tops should be sheathed. \n\n3) The holds are inspected for signs of previous cargo residues. \n\n4) The cargo hold fire-fighting system is thoroughly examined.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "The display of the DSC-controller on board is showing the following lines: RX: 002442000; Ch87; D Sellcall Routine We're asked to listen on: \n\n1) VHF-channel 87 \n\n2) Radio telephony-channel 7 in the 8 MHz band \n\n3) Channel Delta of the coast station \n\n4) VHF-channel 16",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Information about the maximum point loading in cargo holds and on decks of a General Cargo Vessel may be obtained from: \n\n1) General Arrangement plan. \n\n2) Ships Capacity plan.\n\n3) Planned maintenance schedules.\n\n4) Docking plan.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "What should you do with the ashes from your vessels incinerator if you have incinerated garbage containing plastics? \n\n1) Discharge at sea providing you are not in any river or estuary \n\n2) Discharge at sea providing you are more than 12 miles offshore \n\n3) MARPOL demands discharge to a shore facility, regardless of content\n\n4) Discharge at sea providing you are more than 25 miles olishore",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "As per IMDG Code, the term ' separated from' can be defined as: \n\n1) With an intervening compartment, being both a vertical and horizontal separation. Provided an intervening deck is resistant to liquid and fire, a vertical separation of 6 metres is acceptable. For.(on deck) stowage, this segregation means a distance of at least 12 metres irrespective of compartment divisions. \n\n2) Effectively segregated so that the incompatible goods cannot interact dangerously in the event of an accident, but may be transported in the same comparment or hold or on deck, provided a horizontal separation, projected vertically, of 3 metres is obtained.\n\n3) Either in a vertical or horizontal separation: if the intervening decks are not resistant to fire and liquid, then only in a longitudinal separation is acceptable. For (on deck) stowage, this means a distance of at least 12 metres. This distance also applies to one package stowed (on deck) and another in an upper compartment.\n\n4) In different compartments or holds when stowed (under deck). Provided an intervening deck is resistant to fire and liquid, a vertical separation may be accepted as equivalent. For (on deck) stowage, this segregation means a distance of at least 6 metres.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "For which ships is the SOLAS convention applicable? \n\n1) For all vessels. \n\n2) For tankers and other vessels carrying persistent oil as cargo. \n\n3) For passenger vessels only. \n\n4) For all vessels except passenger vessels.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "As a result of being in collision with your vessel, the other vessel involved is on fire? What are your responsibilities to it? \n\n1) You should continue on with the voyage if your damage is not serious \n\n2) The other vessel is in distress and if possible I will render assistance \n\n3) Your vessel should manoeuvre close to the other vessel and aid the fire fighting operation \n\n4) There is no statutory requirement t to provide assistance as the actions of that vessel were the primary cause of the collision",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "In area A1 the function (Transmission of ship to shore distress alerts) is mainly based on: \n\n1) The use of portable VHF \n\n2) The use of HF DSC \n\n3) The use of VHF DSC \n\n4) The use of SART transponders",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "During helicopter evacuation of an injured man, what course should the ship steer? \n\n1) Directly into the wind \n\n2) With the wind fine on the bow opposite to the helicopter operating area \n\n3) With the wind astern so that the effect of the wind is reduced as much as possible \n\n4) As instructed by the helicopter pilot",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Substances, materials and articles shall be stowed as indicated in the Dangerous Goods List of the IMDG Code, in accordance with a series of stowage categories, which are designated as: \n\n1) 5 categories, labelled A-E. \n\n2) Three categories, numbered I, II and III. \n\n3) 10 categories, numbered 1-10. \n\n4) 10 categories, labelled A-K (excluding 1).",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "It is the Master's responsibility to ensure that: \n\n1) All personnel participate in the training at the same time \n\n2) concerned personnel carry out the on- board traing progamme effectively \n\n3) All information reagrding the onboard training is given to the ship manager \n\n4) safety equipment is not used during the training",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "What actions should be taken by the Officer of the Watch if the ship's steering system totally fails? \n\n1) Request the engine room to check the steering system \n\n2) Display the NUC signal and stop the engine(s) \n\n3) All of the suggested answers \n\n4) Call the Master and advise them of the situation",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "On General Cargo ships, cargoes such as logs, fish meal, scrap metal and bales of cotton commonly tend to cause: \n\n1) Large instantaneous fires. \n\n2) Spontaneous combustion. \n\n3) Heavy amounts of ship's sweat. \n\n4) Oxygen depletion in the cargo holds.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "A distress call has been sent accidentally on your MF DSC equipment. Which of the following is correct for cancelling the false distress alert? \n\n1) Make broadcast on 2182 kHz (Mayday all stations...) and cancel the false distress alert. \n\n2) Switch off the transmitter \n\n3) Send a all stations urgent priority MF DSC call \n\n4) Send a selective distress priority MF DSC 4 call to the nearest MRCC-Inform it that a false distress alert has been transmited",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "What is the disadvantage of using chemicals on an oil-spill on the water? \n\n1) It is difficult to apply the chemicals if the oil drifts away from the ship's side \n\n2) The chemicals make it difficult to remove the oil from the water  \n\n3) The water gets a white colour, which makes it easy to detect the oil-spill \n\n4) It is difficult to apply chemicals if there is any wind",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "How often shall each member of the crew participate in an (abandon ship)-drill? \n\n1) Once every week \n\n2)  Once a year \n\n3) Once every month \n\n4)  Once every 6 months",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Why does a vessel slow down in shallow water even though the engine revolutions stay the same? \n\n1) Because there is increased wave action \n\n2)  It does not, it stays at the same speed \n\n3) The propeller thrust is reduced because of the increased water density \n\n4) Because the vessel's hull starts to interact with the sea floor",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Who is the leader of the lifeboat drill (abandon ship drill)? \n\n1) The appointed lifeboat commander. \n\n2) The first member of the crew arriving at  the survival craft. \n\n3) Sen.Off.Deck. \n\n4) Sen.Off.Engine.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "What is the period of validity of the Safety Management Certificate \n\n1) 2 years \n\n2) 5 years \n\n3) 1 Year \n\n4) 6 months",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "A lead battery of 200 Ah, in accordance with the DIN-standard, must be able to supply: \n\n1) 1 ampere during 200 hours \n\n2) 200 ampere during I hour \n\n3) 10 ampere during 20 hours \n\n4) 6 ampere during 20 hours",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "What does STCW deal with? \n\n1) STCW deals with training centre and schools and standards for watch keepers \n\n2) STCW deals with minimum  recommendation for training centre and schools \n\n3) STCW deals with minimum recommendation for training centre and schools \n\n4) STCW deals with minimum recommendation of education for seafarers and minimum standards for training centre and schools",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "You receive a distress alert on HF Radio. What should you do? \n\n1) Wait three minutes and if no acknowledgement is heard from a coast station you should relay the alert. \n\n2) Relay the message immediately on 22182 kHz. \n\n3) Acknowledge receipt. \n\n4) No response is necessary providing the vessel is more than 24 hours away",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Proper guidance on the stowage and securing of general cargo may be obtained by referring to: \n\n1) IMO Code of Practice for Bulk and General Cargoes. \n\n2) IMO Code of practice for stowage and securing of cargoes. \n\n3) International Load Line Regulations. \n\n4) International Load Line Regulations.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Which personnel must undergo familiarization training on board \n\n1) Only the deck officers \n\n2) Only catering staff  \n\n3) Everyone \n\n4) Only the ratings",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Which international convention deals with pollution prevention? \n\n1) ISGOTT. \n\n2) STCW.  \n\n3) SOLAS.\n\n4) MARPOL.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "The two main considerations when choosing an appropriate paint for a cargo space of a General Cargo vessel would be: \n\n1) Light reflective and compatible with edible cargoes. \n\n2) Corrosion resistant and heat resistant. \n\n3) Easy to clean and dark in colour.\n\n4) Low odour and heat resistant.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "If W = Displacement, L = length, B = Breadth, D = depth of vessel, Cb = Block Coefficient, Cw = Coefficient of Waterplane, RD = Relative Density, then: \n\n1) W-LxWxDxCB \n\n2) W=LxBxDxCB/RD \n\n3) W=LxWxDxCW \n\n4) W=LxWxDxRD",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "The MF/HF-transceiver on board is tuned to the assigned frequency of a station. To make this connection the following mode is used: \n\n1) H3E \n\n2) G3E \n\n3) J3E \n\n4) J2B",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Your vessel has been involved in a minor collision. What will your actions be following the collision? \n\n1) Continue the voyage to your destination monitoring for water ingress \n\n2) Call the Company DPO and the local state if close to the coast \n\n3) Make sure your vessel crew are safe and then offer your assistance to the other vessel \n\n4) All of the answers are correct",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "The minimum information to that must be provided be given on a dangerous goods declaration on a General Cargo Vessel should be: \n\n1) IMO Class, UN Number, Gross weight, number of units of cargo, Proper Shipping Name.\n\n2) Gross and net weight, volume of cargo, proper shipping name. \n\n3) IMO Class, weight, cargo brand name, stowage requirement. \n\n4) UN Number, Volume of units, stowage requirements, weight, centre of gravity.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "IMO recommendations on allowance for water absorption in timber deck cargoes on a General Cargo Vessel state that: \n\n1) 10% additional weight should be used in stability calculation for the arrival \n\n2) 15% additional weight should be used in stability calculation for the arrival condition. \n\n3) 5% additional weight should be used in stability calculation for the arrival condition \n\n4) 25% additional weight should be used in stability calculation for the arrival condition.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "What is a Declaration of Security? \n\n1) A checklist jointly completed by the Ship Security Officer and the U.S. Coast Guard \n\n2) A document between the port and the cargo owner stating security \n\n3) A checklist jointly completed by the ship and shore security representatives \n\n4) A document stating the ship's security level",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "What type of vessel is identified by the displayed shapes? \n\n1) A vessel restricted in its ability to manoeuvre \n\n2) A vessel that is constrained by draught \n\n3) A vessel that is engaged in towing \n\n4) A vessel not under command",
                           "https://t.me/picturesforbo/85", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Give the meaning of the following symbol\n\n1) Survival craft portable radio \n\n2) Rocket parachute flare \n\n3) Survival craft distress pyrotechnic signals \n\n4) EPIRB",
                           "https://t.me/picturesforbo/86", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "How often must the Emergency Steering Gear be tested, and how is this information recorded in the OLB? \n\n1) Fortnightly, with signature of Chief Engineer and witness \n\n2) Fortnightly, with signature of Chief Engineer and witness \n\n3) Monthly, with signature of Chief Engineer and witness. \n\n4) Monthly with signature of person carrying MOSS out test",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "In case of a pollution in US waters, who shall notify the cleaning up contractor (OPA-90) \n\n1) Emergency response team \n\n2) The Master  \n\n3) Qualified Individual \n\n4) The shipowner",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Who is responsoble for maintaining the vessels structural strength? \n\n1) The classfication society. \n\n2) The management company  \n\n3) The flag administration. \n\n4) The master.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "A message is send by the Inmarset C-set. The land earth station will: \n\n1) Only send a positive delivery notification (PDN) to the sender if the sender requested, so in the send menu \n\n2) The sender has to confirm delivery by sending another separate message \n\n3) Automatically send a positive delivery notification (PDN) to the sender \n\n4) Never send a positive delivery notification (PON) to the sender. The addressed will have to confirm the message through the ground station and request for further information, if desired",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "A general cargo with a large metacentric height (GM) would be expected to have: \n\n1) A fast roll period and small righting levers (GZ Levers). \n\n2) A fast roll period and large righting levers (GZ Levers). \n\n3) A long roll period and small righting levers (GZ Levers) \n\n4) A long rall period and large righting levers.",
                           "https://t.me/picturesforbo/76", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Which of these can be loaded in the same hold of a General Cargo Vessel, as steel coils? \n\n1) Chemicals \n\n2) Hygroscopic cargoes \n\n3) Steel rebars \n\n4) Fertilizers",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Under the IMO ECDIS requirements, what are the three minimum inputs required? \n\n1) A Position fixing, radar over-lay and log value \n\n2) Gyro heading, compass heading and position information \n\n3) Log speed, distance run and position information  \n\n4) Position fixing, heading and speed information",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "How many square metres does the IAMSAR Volume 3 manual suggest may be calmed by releasing 200 litres of lubricating oil slowly through a rubber hose with the outlet maintained just above the surface while the ship proceeds at slow speed? \n\n1) Approx 5,000 square metres \n\n2) Approx 500 square metres \n\n3) Approx 50,000 square metres \n\n4) Approx 50 square metres",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "In what language/languages must the fire control plans or booklets (or copies of these) be written? \n\n1) In the Flag State official language \n\n2) In the Flag State official language with copies in English or French \n\n3) In a national language where company head office is located  \n\n4) In the English language",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "What type of search pattern is recommended in the IAMSAR Manual as most effective for a single vessel, when the location of the search object is known within relatively close limits? \n\n1) Parallel Sweep Search \n\n2) Sector Search \n\n3) Expanding Square Search \n\n4) Track Line Search",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "On a voyage from hot to cold climate countries, the ventilation of cargo holds of a General cargo ship should: \n\n1) Be carried out during the night time only. \n\n2) Not be carried out at all, \n\n3) Be carried out during the day time only. \n\n4) Be carried out continuously during the voyage.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Eavesdropping and phone taps are examples of which threat to information security? \n\n1) Espionage \n\n2) Subversion \n\n3) Terrorism \n\n4) Sabotage",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "When general cargo is damaged during heavy weather on a General Cargo vessel, it must be ensured that the damage is inspected by the:  \n\n1) Class surveyor. \n\n2) Surveyor representing the vessel's P. & I. Club. \n\n3) Surveyor representing the vessel's hull & machinery underwriters \n\n4) Surveyor representing the consignee.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "On a voyage from cold to hot climate countries, the ventilation of cargo holds of a General cargo ship should: \n\n1) Be carried out continuously during the voyage. \n\n2) Be carried out during the day time only. \n\n3) Not be carried out at all.  \n\n4) Be carried out during the night time only.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "A member of the bridge team has just seen a person fall overboard. Which of the following manoeuvres is the most appropriate to assist with a rescue? \n\n1) Williamson turn \n\n2) Scharnow Turn\n\n3) Evinrude Turn \n\n4) Direct Turn",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "The position that is determined by built in GPS-receiver in an Inmarsat-EPIRB has an accuracy of about: \n\n1) 200 meters \n\n2) 4200 meters \n\n3) 2200 meters \n\n4) 1200 meters",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "A wire aerial for an MF/HF-transmitter must be suspended between isolators: \n\n1) To make the way for aerial currents as long as possible \n\n2) To prevent contact with earth \n\n3) To save energy \n\n4) To prevent burns when touching the aerial",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "All designated SAR aircraft and civil aircraft carry equipment operating on the international aeronautical distress frequencies (amplitude modulation). The aeronautical distress frequencies are? \n\n1) 123.8 MHz and/or 247.6 MHz \n\n2) 243.1 MHz and/or 486.2 MHz \n\n3) 121.5 MHz and/or 243.0 MHz \n\n4) 127.8 MHz and/or 349.6 MHz",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "On a general cargo ship, operating the heavy lift derricks with the boom close to horizontal could result in: \n\n1) The operator having a restricted view of the lifting operation. \n\n2) Damage to the cargo by ship structures. \n\n3) Sudden loss of stability of the vessel. \n\n4) Excessive stresses acting on parts of the derrick system.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Under what convention is the master to ensure that a ship is seaworthy and in a fit state to safely carry a shipper's cargo? \n\n1) The Hague-Visby Rules.  \n\n2) The Antwerp Convention. \n\n3) The Nassau Protocol.  \n\n4)  The Paris Memorandum.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "What spheroidal datum should the GPS receiver be set into, to enable its readout position to be plotted on a paper chart? \n\n1) Select the same datum that the paper chart has  \n\n2) Select WGS84 datum, then when plotting, apply any corrections shown on the chart \n\n3) Set the datum of the country or area that the vessel is in  \n\n4) Select the European datum as this is similar to the WGS84 datum",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "What is the correct setting of the (Anti sea clutter) control on the radar?  \n\n1) A removal of all the sea returns up to about three miles from own-ship \n\n2) No sea returns left on the screen so that a small target will be seen \n\n3) A few sea returns remaining around the own-ship position \n\n4) All of the suggested answers",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "When sending an OBS (weather report) with Inmarsat one should use Service Code '41'. With this address the weather report will always be transmitted to: \n\n1) The meteorological office of the ship's flag state \n\n2) MET office Washington, this office will take care of further dispatch of the weather reports \n\n3) KNMI in Holland \n\n4) The meteorological station connected with the CES used",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "What signal may be given by sound and by light to indicate that a vessel fails to understand the intentions or actions of another vessel, or is in doubt that sufficient action is being taken by the other to avoid collision? \n\n1) Five short and rapid blasts (flashes) \n\n2) Five prolonged blasts (flashes) \n\n3) One prolonged blast (flash), followed by five or more short and rapid blasts (flashes) \n\n4) Three short and rapid blasts (flashes)",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "DG placards shall be located on a freight container: \n\n1) One of the back end and one on any of the sides (only). \n\n2) One on each end and one on each side. \n\n3) One on each side-(only).\n\n4) One on each end (only)",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "When during transmitting the display of a radiotelephone-installation shows a decrease in transmitting power it is: \n\n1) An indication of chosing a wrong channel \n\n2) An adjustment of the semi-duplex transmitting power \n\n3) An indication of aerial problem.\n\n4) An automatic adjustment of the chosen ove transmitting mode",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "The good operation in any location, whether the NAVTEX is working properly or not, can be checked using: \n\n1) Test transmissions specially broadcast for this purpose once a week \n\n2) A compulsory built-in alarm for defects \n\n3) A company test procedure\n\n4) A testing program built in for this purpose",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Prior to loading heavy lift cargoes on a General Cargo Vessel, it must be ensured that: \n1)There are minimum free surface moments in tanks. \n\n2) The vessel is listed to the side to which the load is to be lifted. \n\n3) The vessel has a small metacentric height( GM). \n\n4) All double-bottom tanks are empty.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "A received DSC 'distress alert' contains the following information: (UNDESIGNATED DISTRESS) Of this distress case: \n\n1) The position is unknown \n\n2) The nature of distress is unknown  \n\n3) Time is unknown \n\n4) Number of person at risk is unknown",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "During test and/or maintenance work of the CO2 system affecting the release system, precautions to ensure that the gas is not released into the engine room due to a mistake are to be ensured. What precautions should be taken? \n\n1) Check the main valve for a potential leakage \n\n2) Arrange a watchman in the CO2 central. \n\n3) The main supply line to be blanked off prior to the work.\n\n4) No special precautions necessary.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "A General Cargo vessel is deemed to be cargo worthy when: \n\n1) The hatch covers and/or hatch pontoons are watertight \n\n2) The vessel's Safety Construction Certificate is valid. \n\n3) All her certificates are in order.\n\n4) The hatch covers and/or hatch pontoons are weather tight.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "The compensation payment by the charterer that is due when a vessel is unable to load/ discharge her cargo within the allowed and contracted time is referred to as: \n\n1) Demurrage. \n\n2) Contractual penalty discount. \n\n3) Discretion. \n\n4) Deferment.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "At what calendar interval is a class renewal/ Special Survey required?  \n\n1) Annually. \n\n2) 5 years. \n\n3) Every 2 1/2 years. \n\n4) At 20 years and every five years thereafter.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "If a DSC distress alert is received on board your ship, what is the first action that should be taken? \n\n1) Determine how close your vessel is to the 3 distressed vessel. \n\n2) Immediately answer the distress message on the correct radio frequency  \n\n3) Listen for a distress message on the appropriate radio frequency for five minutes \n\n4) Contact SAR Authorities via nearest coast Radio station",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "DSC uses for automatic identification the MMSI. The identification 002442000 is assigned to: \n\n1) A type of vessel's \n\n2) A vessel \n\n3) A group of vessels \n\n4) A coast-station or coast guard-station",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "One of the categories of information that must be included in your SSP is: \n\n1) Security arrangements \n\n2) Ship security survey \n\n3) Threat scenarios \n\n4) Weaknesses in security measures",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "In area A2, the function (Transmission of ship to shore distress alerts) is mainly based on: \n\n1) The use of VHF DSC \n\n2) The use of MF DSC \n\n3) The use of SARSAT COSPAS Epirbs \n\n4) The use of INMARSAT Epirbs",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "In radio telephony what is the (URGENCY CALL) which should be used to indicate that you have a very urgent message to transmit concerning the safety of another vessel or person? \n\n1) Victor Victor (3 times) \n\n2) Mayday (3 times) \n\n3) Pan Pan (3 times) \n\n4) Security 13 times)",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Why is it important to have good a relationship between the crew on board a vessel? \n\n1) Crew comes to know each others problems \n\n2) It will prevent accidents from happening \n\n3) It encourages crew to extend their contract \n\n4) It leads to better work performance and positive atmosphere among the crew",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "On area A3 the function (Transmission and reception of signals for locating) is mainly based on: \n\n1) the use of SART transponders \n\n2) the use of SARSAT COSPAS Epirbs \n\n3) the use of MF DSC \n\n4) the use of HF DSC",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "The emergency battery of a GMDSS portable radio: \n\n1) Cannot be replaced \n\n2) Must be replaced before the expiry date is exceeded \n\n3) Must be tested once a week \n\n4) Must be charged after expiry date",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "By a 'geographical area call' in the DSC system is meant: \n\n1) A DSC- message for all ships in a particular ocean region \n\n2) A DSC-message for all vessels within a certain area from a position in the DSC message, and the degrees are given in northerly and westerly direction \n\n3) A DSC- message for all vessels within a certain area marked by a reference position, given in the DSC message and the degrees are given in southerly and easterly direction \n\n4) A DSC- message for all ships heading towards a certain geographical area",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "On area A3 the function (Reception of shore to ship distress alerts) is mainly based on: \n\n1) The use of SARSAT COSPAS Epirbs and NAVTEX \n\n2) The use of MF DSC and INMARSAT C SAFETYNET \n\n3) The use of VHF DSC and NAVTEX \n\n4) The use of HF DSC and INMARSAT C SAFETYNET",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "In area A1 the function (Reception of shore to ship distress alerts) is mainly based on: \n\n1) the use of VHF DSC \n\n2) the use of SART transponders \n\n3) the use of SARSAT COSPAS Epirbs \n\n4) the use of MF DST",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "On board an accident happened. Urgent radio-medical advice is needed. We choose the category: \n\n1) Routine \n\n2) Urgency \n\n3) Distress \n\n4) Safety",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Which of following are security duties? \n\n1) Monitoring of restricted areas \n\n2) All alternatives  \n\n3) All alternatives \n\n4) Checking ID of visitors onboard",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Which personnel must undergo familiarization training on board? \n\n1) Only catering staff \n\n2) Only the ratings  \n\n3) Everyone \n\n4) Only the deck officers",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "What can lead to (Unlimited responsibility) (OPA-90) \n\n1) Only wilful misconduct \n\n2) Only gross negligence  \n\n3) Wilful misconduct and gross negligence \n\n4) Wilful misconduct, gross negligence and violation of Federal Safety",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Who is responsible for ensuring your ship completes a security assessment? \n\n1) Company Security Officer \n\n2) Flag State Administration  \n\n3) Ship Security Officer \n\n4) Recognized Security Organization",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "You are on a vessel 10 nautical miles off the coast of Nigeria, West Africa. Are you allowed to dump empty glass bottles overboard? \n\n1) Yes, glass bottles can be dumped overboard \n\n2) No, glass bottles can not be dumped overboard  \n\n3) Yes, the bottles can be dumped if they are ground so that the resulting particles can pass through a screen with 25 mm openings  \n\n4) Yes, the bottles can be dumped if they are ground so that the resulting particles can pass through a screen with 50 mm openings",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Check the items that can be a possible threat \n\n1) Bombing and Sabotage \n\n2) (Piracy, Hijacking and Smuggling) \n\n3) All alternatives \n\n4) Cargo tampering and Stowaways",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Onboard training should be organised in such a way that: \n\n1) Each crew member is trained individually \n\n2) none of the above \n\n3) It does not contravene with the rest hours of the crew and each crew member is trained individually \n\n4) It is an integral part of the overall training plan and does not contravene with the rest hours of the crew",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "On area A4 the function (Transmission and reception of signals for locating) is mainly based on: \n\n1) The use of SART transponders \n\n2) The use of SARSAT COSPAS Epirbs \n\n3) The use of HF DSC \n\n4) The use of MF DSC",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "The first step in completing an SSA is to: \n\n1) List the existing security measures.\n\n2) Create a list of potential motives for security incidents against your ship. \n\n3) Identify the key shipboard operations, systems, areas and personnel that are critical to protect. \n\n4) Develop an onboard security survey checklist",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Which of the following two digits codes is used to obtain medical advice? \n\n1) 38 \n\n2) 26 \n\n3) 32 \n\n4) 42",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Who is responsible for issuing an ISPS certificate? \n\n1) US Coast Guard \n\n2) The insurance company \n\n3) The Port State \n\n4) The Flag State",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Ships of 10.000 tons gross tonnage and more, shall be fitted with oil filtering equipment, complying with Reg.14 (7) of MARPOL for the control of machinery space bilges. What would be the maximum oil content oil-water mixture to pass through the filter? \n\n1) 15 ppm \n\n2) 100 ppm\n\n3) 30 ppm \n\n4) 60 ppm/n.m",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "On area A4 the function (Transmission of ship to shore distress alerts) is mainly based on: \n\n1) The use of HF DSC and INMARSAT Epirbs \n\n2) The use of HF DSC and COSPAS SARSAT Epirbs \n\n3) The use of MF DSC and INMARSAT Epirbs \n\n4) The use of VHF DSC and VHF Epirbs",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Which international convention deals with fire-fighting equipment etc. \n\n1) Load Line convention \n\n2) CRYSTAL \n\n3) SOLAS \n\n4) MARPOL",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "On area A4 the function (Transmission and reception of on scene communications) is mainly based on:\n\n1) the use of HF DSC \n\n2) the use of SARSAT COSPAS Epirb \n\n3) the use of MF and/or HF R/T \n\n4) the use of HF/MF and/or VHF R/T",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "The steps of the embarkation ladder used must be spaced apart by a distance of: \n\n1) Equally spaced and not less than 300 mm or more than 380 mm \n\n2) equally spaced, not less than 200 mm or more than 280 mm \n\n3) 200 mm \n\n4) 300 mm",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "For the same vessel and the same rudder angle, is the diameter of the turning circle completed at full ahead smaller than one completed at half ahead? \n\n1) Yes, it would be a much smaller turning circle at half ahead \n\n2) No, the diameter of the turning circle would be almost the same. \n\n3) Yes, there would be a change of shape of the turning circle; it would have an increase in the transfer, but not the advance.\n\n4) No, it will be much larger turning circle at half ahead",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "In the situation illustrated with a ship on even keel, how should the tug power be set to enable the vessel to be pushed sideways without changing its heading? \n\n1) It would be very difficult to predict which 2 tug needs greater or lesser power, it would have to be trial and error  \n\n2) Usually there would be greater power on the aft tug than on the forward tug \n\n3) Usually there would be greater power on the forward tug than on the after tug \n\n4) Equal power required by both tugs as 4 they are the same distance from bow and stern",
                           "https://t.me/picturesforbo/102", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "What are the functions of a flag state administration?  \n\n1) The have responsibility for ensuring that ships are correctly manned and that crews terms and conditions of employment are met satisfactorily \n\n2) They have responsibility for ensuring that ships are properly registered \n\n3) The maintain a record of all ship and their crews, and produce statistics involving ships from their country \n\n4) They have responsibility for setting. monitoring and enforcing standards of safety and pollution prevention on vessels flying the countries flag",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Which type of profiling is used to obtain information about rival companies and their employees? \n\n1) Industrial \n\n2) General \n\n3) Commercial \n\n4) Criminal",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "You are on a vessel 10 nautical miles off the coast of Algeria, in the Mediterranean Sea. Are you allowed to dump food waste overboard? \n\n1) Yes, all kind of food waste can be dumped overboard \n\n2) No, food waste can not be dumped overboard \n\n3) Yes, the food waste can be dumped if it is ground so that the resulting particles can pass through a screen with 50 mm openings \n\n4) Yes, the food waste can be dumped if it is ground so that the resulting particles can pass through a screen with 25 mm",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "How frequently should reports from protection and environmental work be sent to shore based management? \n\n1) Every three years. \n\n2) Not mandatory to send reports \n\n3) Annually. \n\n4) Biannually.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "OPA-90 is referring to a Qualified Individual (QI) \n\n1) Ql is the owner's contingency leader \n\n2) Ql is representing the USCG \n\n3) An individual certified by USCG to handle oils spills \n\n4) Ql is an authorised individual, situated in the US, and contracted by the owner or operator of the vessel",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "What is the action that a GMDSS Radio Operator should take when a DSC distress alert is received? \n\n1) The Operator should immediately set continuous watch on VHF channel 70. \n\n2) The Operator should immediately set continuous watch on the NBDP frequency that is associated with frequency band on which the distress alert was received. \n\n3) The Operator should immediately set continuous watch on the radiotelephone frequency that is associated with frquency band on which the distress alert was received. \n\n4) No action is necessary, as the DSC control will automatically switch to the NBDP follow-on communications frequency.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Are there any exceptions from OPA-90 \n\n1) No exceptions \n\n2) Yes, transit passage through US watst a non US port \n\n3) Yes, if the vessel calls a US port for only a short  \n\n4) Yes, close to any US naval base",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "In which areas is plastic material accepted for overboard disposal? \n\n1) In coastal waters. \n\n2) In specially designated areas (ref. MARPOL), \n\n3) Not permissible any where.  \n\n4) 100 n.m. from shore line.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "HEL-H is the abbreviation of a heavy helicopter radius of action for rescue purposes. What do you think the radius and evacuating capacity of the helicopter is? \n\n1) 100 nm and capacity for evacuating \n\n2) 500 rim and capacity for evacuating more than 25 persons. \n\n3) 150 nm and capacity for evacuating more than 12 persons.  \n\n4) 200 nm and capacity for evacuating more then 15 persons.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "The purpose of profiling is to? \n\n1) Get beneath the outer shell of an individual to obtain a more complete picture. \n\n2)  Identify different personality types. \n\n3) Categorize people based on their nationality and ethnicity.  \n\n4) Make judgements about people based on heir appearance.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "What manoeuvre should be carried out in case of a fire onboard a ship? \n\n1) Continue on course and speed \n\n2) Reduce speed and, if possible, keep the fire zone to the leeward of the ship \n\n3) Let the ship follow the wind in order to reduce the oxygen supply  \n\n4) Keep the stem up against the wind if possible",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "What is the emergency channel on VHF? \n\n1) Channel 21 \n\n2) Channel 09 \n\n3) Channel 16  \n\n4) Channel 69",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "What is a Continuous Synopsis Record? \n\n1) A record of all security incidents \n\n2) A plan for continuous maintenance of security equipment \n\n3) A plan including all security measures onboard \n\n4) A record of the vessels history",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "A distress alert sent by Inmarsat to an RCC is sent via: \n\n1) LES \n\n2) NCS \n\n3) The managers office \n\n4) LUT",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "The ship is approaching shallow water where the Under Keel Clearance will reduce to about 0.25 of the ship's draught. Which of the following answers most accurately summarizes the aspects to be considered when deciding a suitable speed? \n\n1) Touching the bottom if there is any swell and causing damage due to wash of the vessel the wake or \n\n2) All of the suggested answers \n\n3) A further reduction of underkeel 3 clearance and possible changes of the ship's trim \n\n4) A reduced ability to stop the vessel and maintain steerage",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "The DoS addresses the responsibility for the security of the water around the ship and the verification of increased threat levels. \n\n1) FALSE \n\n2)  \n\n3) TRUE \n\n4)",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Your vessel is power-driven and making way in open water. This vessel is on the port bow with a steady bearing. What kind of vessel is it and what will your action be? \n\n1) This is a vessel engaged in fishing. It is my responsibility to keep clear under rule 18 and I will alter course to starboard, sounding one short blast \n\n2) This is a sailing vessel underway. I am the stand-on vessel and will maintain my course and speed under rule 17  \n\n3) This is a sailing vessel not making way 2 through the water. There is no risk of collision and I will maintain my course and speed \n\n4) This is a sailing vessel underway, seen head-on. It is my responsibility to keep clear under rule 18 and I will take appropriate avoiding action",
                           "https://t.me/picturesforbo/87", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "According to rule 13 of the International Regulations for Preventing Collisions at Sea, what is the definition of (an overtaking vessel)? \n\n1) When coming up with another vessel from a direction more than 22.5 degrees abaft its beam \n\n2) When coming up with another vessel from a direction more than 45 degrees abaft its beam  \n\n3) When the vessel is detected as a radar target or sighted visually in a position directly astern \n\n4) When coming up with another vessel from any direction abolt its beam",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Which of these conventions is The International Ship and Port Facility Security (ISPS) Code a part of? \n\n1) MARPOL \n\n2) SOLAS  \n\n3) The Anti Terrorist International Agreement \n\n4) STCW-95",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "On area A2 the function (Transmission and reception of on scene communications) is mainly based on: \n\n1) The use of MF DSC \n\n2) The use of SART transponders  \n\n3) The use of MF and/or VHF R/T \n\n4) The use of VHF DSC",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Regular 'updating' of a ships' position in an Inmarsat-C installation is necessary \n\n1) To enter the correct data to the disk antenna \n\n2) To keep to the correct Inmarsat-region \n\n3) To inform the satellite of ships position \n\n4) To have the correct position in case of accidents",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Who is responsible for ensuring that your ship's security plan meets the requirements of the ISPS Code? \n\n1) Company Security Officer \n\n2) Ship Security Officer  \n\n3) Flag State Administration \n\n4) Recognized Security Organization",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "The word SHIP is spelled conform the international phonetic alphabet: \n\n1) Singapore, Hotel, India, Paris \n\n2) Sierra, Hotel, India, Papa \n\n3) Sierra, Hotel, Item, Papa \n\n4) Sugar, Hotel, Italia, Peter",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Which of this information must be included in a piracy attack alert? \n\n1) The number of crew onboard. \n\n2) The number of pirates/highjackers. \n\n3) Your ship's name and call sign. \n\n4) The type of weapons being carried by the pirates/highjackera",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "A tug is connected to the bow of a vessel. Will the force exerted by it be the same at any ahead speed? \n\n1) No, when the ahead speed of the ship increases the force exerted by the tug will also increase \n\n2) Yes, the force would normally be expected to be the same at any speed of the ship \n\n3) Yes, because when moving ahead a tug can use indirect towing methods \n\n4) No, on the bow the tug uses power to run with the vessel, which reduces the available power on the towline",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "What is meant by saying that a vessel hull is directionally unstable? \n\n1) When free running it will shear to one side or the other if not controlled \n\n2) It has been intentionally created with the centre of underwater pressure aft of amidships \n\n3) The ship will only require small amounts of helm to maintain its course when stearing in a heavy seaway \n\n4) When the rudder is kept amidships, the ship will continue on a straight course",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "What effect does shallow water have on a normal commercial vessel's turning circle? \n\n1) Turning circle will stay the same as they are a function of the hull length only \n\n2) Turning circles will be of a greater diameter for the same rudder angle \n\n3) Turning circle will stay the same as they are a function of the rudder angle only \n\n4) The effect totally depends upon the 4 shape of the hull, a lot of hulls are not effected",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Any ship of 10.000 tons gross tonnage and above shall be fitted with oily-water separating equipment for the control of machinery space bilges. What kind of equipment is required in this connection? \n\n1) Oil filtering equipment only. \n\n2) Sludge separating tank. \n\n3) Either Oil filtering equipment, or Oily- water separating equipment, or combination of both. \n\n4) Oily-water separating equipment only.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "For a (distress alert) via the DSC, the MF- band is used in the frequencies: \n\n1) TX:2177.0 kHz RX: 2177.0 kHz \n\n2) TX: 2189.5 kHz RX: 2189.5 kHz \n\n3) TX: 500.0 KHz RX: 518.0 KHz\n\n4) TX: 2187.5 kHz RX: 2187.5 kHz",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "What is EPIRB an abbreviation for? \n\n1) Emergency Position Indicating Radio Beacon. \n\n2) Electronic Pressure Indication Radar Buoy.\n\n3) Electronic Purpose If Rescue Begins. \n\n4) Emergency Position Indication Radio Buoy",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "According to the International Regulations for Preventing Collisions and the illustrated lights, what type of vessel is this? \n\n1) This is a fishing vessel, not making way through the water, with its nets fast upon an obstruction, seen from astern \n\n2) This vessel is not under command and is not making way through the water \n\n3) This vessel is aground and is seen from directly ahead  \n\n4) This vessel is restricted in its ability to manoeuvre and is stopped in the water. I am seeing it from astern",
                           "https://t.me/picturesforbo/103", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Which type of call will be sent by a ship in danger of capsizing and needing assistance from all vessels in her vicinity? \n\n1) Distress relay call \n\n2) Safety call \n\n3) Distress call \n\n4) Urgent call",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Which of following items shall be included in an abandon ship drill? \n\n1) Checking the distress signal rockets and other distress signais \n\n2) Checking the lifeboat provisions and supplies \n\n3) Checking passenger's immersion suits \n\n4) instruction in the use of radio life- saving appliances",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Records relating to breaches of security and changes in security level must be secured against unauthorized access and available for review by contracting governments. \n\n1) TRUE \n\n2) FALSE \n\n3)  \n\n4) ",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Which of the following is a coast station MMSI? \n\n1) 227005300 \n\n2) 002275300 \n\n3) 227530000  \n\n4) 22753000",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "The International Maritime Bureau Piracy Reporting Centre attributes the increased numbers of hijackings to: \n\n1) More crew involvement. \n\n2) Easy access to military weapons. \n\n3) The greater involvement in piracy of well- organized and armed crime networks.  \n\n4) Higher crime rates around the world.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Which of the following duties shall be included in the (muster list) as being assigned to members of the crew? \n\n1) Preparation of immersion suits for the ship's passengers \n\n2) Preparation of manoeuvres intended to ease launching of the survival craft  \n\n3) Operation of the vessel's propulsion system  \n\n4) Preparation and launching of the survival craft",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "To guarantee optimal reception of VHF-DSC- calls, every: \n\n1) DSC-symbol is sent twice and checked extra by Error Check Character \n\n2) DSC-report is sent twice, at least every. second call is compared with the earlier received call \n\n3) DSC-calls are repeated untill received  \n\n4) DSC-symbol is checked on the right amount of , and then checked on the correct relation by Error Checked Character ",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Why does a ship with ahead or astern speed, have a small lateral or sideways movement when turning. \n\n1) The ship moves laterally because of all the external forces on the vessel hull caused by the environment and possibly a tug \n\n2) The hydrodynamics of the hull cause a drift angle to be produced, which is not in the fore and aft line of the vessel  \n\n3) Because the rudder is positioned at the stern of the vessel \n\n4) The ship moves laterally because it has a single hull",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "The distress message is used when the vessel is threatened by a serious and imminent danger and is in need of immediate assistance. What is the telephony distress signal? \n\n1) PAN-PAN \n\n2) SECURITY \n\n3) MAYDAY  \n\n4) RESCUE-RESCUE",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Which of the following information shall be specified by the muster list? \n\n1) The muster list has been prepared and approved by the administration before the ship proceeds to sea \n\n2) The abandon ship signal consisting of two long blasts \n\n3) The specific duties assigned to passengers that are in charge of a group of others  \n\n4) Action to be taken by crew and passengers",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "The names and addresses of accounting authorities can be found in: \n\n1) The ITU List of Ship Stations \n\n2) The ITU List of Coast Stations \n\n3) The ITU List of Callsigns and Numenical Identities of Stations used by the Maritime Mobile and Maritime Mobile-Satellite Services \n\n4) The ITU List of Radiodetermination and Special Services",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "What is the top priority if an incident occurs in US waters (OPA-90) \n\n1) Any immediate action to prevent loss of time \n\n2) Safety of ship and crew \n\n3) Protection of the environment \n\n4) Prevention of oil pollution",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "A contractor is hired to install new navigation equipment onboard your ship while it's berthed. For a period of time he's left unsupervised and photographs schematics of the ship that he finds rolled up and stored in the corner of a nearby office. Later, from home, he hacks into the network and prints off information about the ship's security procedures. Which of these information security measures would have prevented his unauthorized access? \n\n1) Firewall, protective markings, vetting and a secure network. \n\n2) Secure area, passwords, a firewall and protective markings. \n\n3) Secure area, passwords, a firewall and a secure network. \n\n4) Protective markings, reference checks, and passwords.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "The correct order of actions to be taken in a fire emergency, should be... \n\n1) Extinction, evaluation of the situation, confinement of fire, rescue and life- saving \n\n2) Evaluation of the situation, confinement of fire, rescue and life-saving, extinction \n\n3) Extinction, confinement of fire, feed back on the emergency, rescue and life- saving, then evaluation of the situation \n\n4) Evaluation of the situation, rescue and life-saving, confinement of fire, extinction, then feed back on the emergency",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "For calling a coast-station by VHF one should preferably use: \n\n1) A working channel of the nearest shore- station of that coast-station \n\n2) A special calling channel of that coast-station \n\n3) Channel 70 \n\n4) Channel 16",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "In case of pollution in US waters, do you always have to notify the National Response Center (OPA-90) \n\n1) No, only the shipowner can notify NRC \n\n2) Yes, within thirty (30) minutes \n\n3) No, not if the local US State Authority is correctly notified \n\n4) Yes, within three (3) days",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "When a SOLAS vessel is required to have an emergency tow, what would be the best way to connect a tug? \n\n1) Using a bridle made up from the vessel's 2 anchor chains \n\n2) With the towline led around the base of the windlass pedestal and shackled off \n\n3) Using the vessel's emergency towing arrangement \n\n4) With the towline turned up on a set of bits on the forecastle deck",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Which one of the listed requirements regarding the stowage of a survival craft corresponds to present SOLAS regulations? Each survival craft shall be stowed: \n\n1) Wherever space is available. \n\n2) In a state of readiness that two.crew members can prepare embarkation and launching in less than 15 minutes. \n\n3) On the starboard side of the ship.\n\n4) In a secure and sheltered position and protected from damage by fire or explosion.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Which word will precede an urgency message? \n\n1) PAN PAN \n\n2) URGENCE \n\n3) PAN \n\n4) MAYDAY",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Which of these actions should you take it your ship is successfully boarded by armed pirates? \n\n1) Keep quiet and ignore any questions you're asked. \n\n2) Assure your captors that you're not planning an attack to overthrow them. \n\n3) Fight back. \n\n4) Scream in fear and refuse to cooperate.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "The batteries must be placed in a well ventilated place, so that: \n\n1) The person can work in the compartment \n\n2) The production of detonating gas can be prevented \n\n3) The detonating gas can be discharged  \n\n4) There is sufficient oxygen available for optimum working of the batteries",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "What is a contingency plan for ships? \n\n1) Plan for next voyage \n\n2) Plan for maintenance and repair \n\n3) Loading plan for general cargo \n\n4) Plan for safety preparedness",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "The portable walkie talkies required to be carried by GMDSS regulations should have which channels as a minimum?  \n\n1) Channels 6, 13 & 16 \n\n2) Channel 16 only \n\n3) Channels 13 & 16. \n\n4) Channels 6 & 16",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "In a distress situation, how many times or for how long should the emergency alarm signal be sounded?  \n\n1) 3 times \n\n2) Until all crew members and passengers have reported to their respective muster stations \n\n3) 3 minutes \n\n4) Until the signal (risk is over) or the order 4 abondon ship is given",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Who is responsible that regulatory working hours are not exceeded? \n\n1) The bosun and the second engineer. \n\n2) The individual person.\n\n3) The master and department heads.\n\n4) The safety officer.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "An Oil Record Book, Part 1, shall be provided to every ship of 400 tons gross tonnage and above to record machinery space operations.Out of below mentioned operations, it is compulsory to record: \n\n1) Purification of HFO. \n\n2) Discharge of water from Aft, Peak Tank. \n3) Transfer of oil from settling - to daytank. \n\n4) Bunkering of bulk lubricating oil.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "After confirmation that there is no other radio-traffic, we call on a VHF working channel of a coast-station. When you don't get any reply: \n\n1) You must wait 3 minute minimum before repeating your call \n\n2) You must wait 1 minute minimum before repeating your call \n\n3) You must wait 5 minutes before repeating the call \n\n4) You can repeat your call immediately",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Why shall a duly qualified officer supervise any potential polluting operation? \n\n1) To inform the authorities. \n\n2) To avoid pollution. \n\n3) To restrict pollution.\n\n4) To relieve the master.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Which organization or administration is responsible for surveys and inspections of ships, and the issue of Safety Certificates? \n\n1) International Maritime Organization (IMO) \n\n2) International Labor Organization (ILO) \n\n3) Ships Classification Associations (Lloyd's American Bureau of Shipping. The 2 Norwegian Veritas, Germanische Lloyd's, etc.) \n\n4) Government Authorities of the Flag State",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "*Which of the following detailed explanations should be mentioned in the Training Manual? \n\n1)How to recover survival craft and rescue boats including stowage and securing \n\n2) How to use navigational equipment for survival crafts \n\n3) How to use escape routes and other escape methods \n\n4) How to use surface to air visual signals to be used by survivors",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Shipboard Emergency Drills must be carried out at least (OPA-90): \n\n1) Once a week \n\n2) Once a month \n\n3) Once every six months \n\n4) Once a year",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "The hydrostatic release of an EPIRB should be changed \n\n1) Every four years \n\n2) Every three years- \n\n3) Every two years \n\n4) Yearly",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "What is SITREP an abbreviation for? \n\n1) Ship Indication Transmission Equipment. \n\n2) Ship Transit Emergency Radio \n\n3) Transponder Equipment. \n\n4) Survivor Indication",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Which of these statements about drug smuggling is true? \n\n1) The risks to ships are not restricted to specific areas or trading routes. \n\n2) Drug smuggling is only a problem in certain ports, so only ships sailing in those ports need to implement preventative measures.\n\n3) Drugs are difficult to conceal onboard a ship.\n\n4) The preventative measures you incorporate into your ship's security plan should be exhaustive, regardless of the level of threat identified by your ship's security assessment.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "A Cargo Ship Equipment Certificate will be issued for: \n\n1) 3 years \n\n2) 5 years with control every 12 months \n\n3) 2 years with control every 6 months \n\n4) 4 years",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "What is most important for crew members when preparing for emergencies? \n\n1) That people listen to orders given \n\n2) That people know where to find designated equipment \n\n3) That people are well trained \n\n4) That people know where to muster",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "What is a (passenger) according to SOLAS regulations? \n\n1) Any person holding a ticket and travelling with a passenger ship \n\n2) Any person paying their voyage regardless of ship type \n\n3) Everyone who travels with a passenger ship \n\n4) Every person other than the Captain and the members of the crew or other persons employed or engaged onboard the ship in the business of that ship.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "The most effective way to combat the threat of drug smuggling is to? \n\n1) Perform routine, but irregular searches  using teams of two or more personnel from the same department. \n\n2) Combining routine, but irregular searches of the ship with spontaneous targeted searches. \n\n3) Perform spontaneous targeted searches using teams of two or more personnel from the same department. \n\n4) Organize crew into pairs and conduct weekly searches of the ship",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "As per IMDG Code, the main criteria for drawing up classes for safe handling of hazardous substancesis on the basis of: \n\n1) Chronological order in which they have been assessed. \n\n2) Alphabetical order. \n\n3) The type of hazard they present. \n\n4) Selective laboratory tests commissioned by the Committee",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "How can an ARPA best assist the bridge team to steer a suitable course to make good the entrance to a channel? \n\n1) Use the mapping facility provided by the ARPA, create a map of the channel then display it for entry \n\n2) Alter course so that own-ships water stabilised true vector passes through the entrance to the channel \n\n3) Acquire a buoy at the entrance to the channel and alter course to make the relative vector of the buoy point at own- ship \n\n4) Alter course so that own-ships ground stabilised true vector passes through the entrance to the channel",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Which class of emission is used for VHF DSC transmissions? \n\n1) G2B \n\n2) J3E \n\n3) G3E \n\n4) J2B",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Why should a Ground Stabilised True Motion radar display not be used for anti-collision purposes? \n\n1) Because this display is only ever used for navigation \n\n2) The 'aspect of the target is confused, so the Regulations for Preventing Collisions cannot be accurately applied \n\n3) True motion does not provide the collision risk of targets as only true vectors are available \n\n4) The true vector can never give an indication of collision risk with another ship",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "The word SATCOM is spelled conform the international phonetic alphabet: \n\n1) Sierra, Able, Tripoli, Charlie, Oscar, Mike \n\n2) Sierra, Anna, Tango, Cornelies, Oslo, Mike \n\n3) Sierra, Alfa, Tango, Charlie, Oscar, Mike \n\n4) Sierra, Able, Tango, Cornelies, Oslo, Man",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "A DSC-notice should be sent on VHF-channel: \n\n1) 13 \n\n2) 67 \n\n3) 16 \n\n4) 70",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "What is the required number of hours that a SART's battery must be able to operate the unit in the standby mode? \n\n1) Four (4) days \n\n2) Forty-eight (48) hours \n\n3) Eight (8) hours \n\n4) Three (3) days",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Which two persons check the Declaration of Security? Select the correct pairing. \n\n1) The Local Coast Guard Officer and the Port Facility Security Officer \n\n2) The Port Facility Security Officer and the Ship Security Officer \n\n3) The Company Security Officer and the Ship Security Officer \n\n4) The Company Security Officer and the 4 Port Facility Security Officer",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "According to the International Regulations for Preventing Collisions, when a ship is being overtaken by another while proceeding along a river. What should be the required procedure? \n\n1) There should be no overtaking in these confined waters \n\n2) The overtaking vessel can overtake but must allow sufficient space to reduce the interaction between the two vessels \n\n3) The overtaking vessel should request permission from the other ship by sounding two prolonged blasts followed by two short blasts on the whistle or by direct VHF contact \n\n4) The overtaking vessel should request permission to overtake from the Port Control VTS",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "The pyrotechnics used to transmit visual signals to other vessels, boats or aircrafts are of the following type \n\n1) Rocket parachute flare \n\n2) Buoyant smoke signal \n\n3) Hand flare \n\n4) All of the below mentioned",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "For a search to be effective it must be: \n\n1) Centrally controlled. \n\n2) Inclusive of all personnel. \n\n3) Organized haphazardly. \n\n4) Conducted by personnel with limited knowledge of the ship's layout.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "On an oil tanker outside a special area, what is the maximum instantaneous rate of discharge of oil content per nautical mile? \n\n1) 20 litres per nautical mile. \n\n2) 30 litres per nautical mile \n\n3) 60 litres per nautical mile. \n\n4) 40 litres per nautical mile.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "One can check the functioning of the SART by: \n\n1) Lowering SART in to the sea \n\n2) Removing it from the holder and turning the SART upside down \n\n3) Actvating the SART and checking the effect on the radar screen \n\n4) Activating it by extracting the antenna",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "With an Inmarsat-C terminal the option 'PSTN' for addressing is available. This option: \n\n1) Have the operator read the message by phone \n\n2) Delivers the message as a fax \n\n3) Delivers a message as a telegram \n\n4) Is to deliver a message by telephone via a modem on the computer of the suscriber",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "When onboard channel 16 is used for a shore radio-connection, you always work: \n\n1) Simplex \n\n2) Semi-duplex \n\n3) Duplex \n\n4) On low power",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "The Declaration of Security: \n\n1) Identifies the security responsibilities of shipboard personnel \n\n2) Addresses the security requirements shared between ships or between a port facility and a ship. \n\n3) Details a ship's security measures. \n\n4) States the reporting procedures to government contact points",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "If a ship in the MF-band wants to have a DSC-connection with a coast-station (no 'distress alert' or a test alert) the following frequencies are chosen: \n\n1) Tx: 2187.5 KHz RX: 2182 KHz \n\n2) TX: 2177.0 kHz RX:-2189.5 kHz \n\n3) TX: 2177.0 kHz RX:-2189.5 kHz \n\n4) OTX: 2177.0 kHz RX: 2177.0 kHz",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "The following information must be given on the SART: \n\n1) The date of replacement of the hydrostatic release unit \n\n2) The name of the operator \n\n3) The MMSI number sent \n\n4) Date of replacement of the batteries",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Inmarsat Telex Service code '33' can be used: \n\n1) When technical problems are experienced with the Inmarsat-terminal \n\n2) To ask for maritime enquiries \n\n3) When the coast-station is disfunctional \n\n4) To ask for radio medical advice",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Which of the following items must be included in each fire drill? \n\n1) Reporting to stations and preparing for the duties described in the muster list \n\n2) Starting a fire pump using at least two required jets of water to show that the system is in proper working orde \n\n3) All the items mentioned \n\n4) Checking fireman's outfits and other personal rescue equipment",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Which of the following duties shall be included in the (muster list) as being assigned to crewmembers in relation to passengers? \n\n1) Clearing the escape routes \n\n2) Ensuring that extra food and water is taken to the survival craft \n\n3) Ensuring that every passenger is provided with an immersion suit or a thermal protective aid \n\n4) Assembling passengers at muster station",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "The correct functioning of a DSC-modem can be checked by means of: \n\n1) The built-in test facility in the modem \n\n2) The testing-mode of the ever present VHF DSC-EPIRB \n\n3) The obligatory monthly transmission from the RCC's \n\n4) Tester provided with the equipment",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Which of the following two digits codes is used to obtain maritime assistance? \n\n1) 32 \n\n2) 39 \n\n3) T38 \n\n4) 37",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "When on HF band a DSC distress alert is received, you have to listen to: \n\n1) 8414.5 kHz (DSC distress frequency in 8 MHz \n\n2) The radio-telex distress frequency in the band in which the DSC distress alert was received \n\n3) 2182 KHz \n\n4) The radio telephony distress frequency in the band in which the DSC distress alert was received",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Which type of call will be sent by a ship adrift and needing the assistance of a tug ? (The weather is not bad and the ship will be aground 24 hours later) \n\n1) Urgent call \n\n2) Distress relay call \n\n3) Safety call  \n\n4) Distress call",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "The vessel with the illustrated lights is sighted ahead and slightly to port. What do the lights tell you about the status of the other vessel, and what should happen on your vessel? \n\n1) This is a vessel not under command at anchor \n\n2) This vessel is aground. My vessel should be navigated with extreme caution given the nature of the hazard \n\n3) This is a vessel engaged in fishing vessel, with her nets fast on an obstruction, My vessel should keep out of the way by rule 18 of the International Collision Regulations \n\n4) This is a vessel aground. She appears to have been headed to starboard of my track and my vessel should alter course to port, passing under her stern",
                           "https://t.me/picturesforbo/89", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "What would happen if, when a ship is under- going a Port State Inspection, certificates were invalid or missing \n\n1) The deficiencies would be recorded in the ship's register and the ship allowed to sail \n\n2) The ship would be detained indefinitely \n\n3) Rectification would be required before sailing \n\n4) The ship would be allowed to sail to the next port and rectification would take place then",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Silencing by a station, not in charge of the distress-traffic, is done as follows: \n\n1) (SEELONCE MAYDAY) followed by the silencing station's call-sign \n\n2) (SILENCE DISTRESS) followed by call sign of the ship in distress \n\n3) (SEELONCE MAYDAY) followed by the call-sign of the ship in distress  \n\n4) (SEELONCE DISTRESS) followed by the silencing station's call-sign",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "A distress alert on board may only be transmitted on explicit order of:\n\n1) The captain \n\n2) The radio officer \n\n3) The safety officer.\n\n4) The navigating officer on duty",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Which of the following is the correct minimum carriage requirement for a ship of more than 300 gross tons and operating in area Al: \n\n1) 1 MF RT DSC DSC watch receiver - 1 or 2 2 SART-1 NAVTEX or 1 EGC receiver-2 or 3 VHF portable - 1 EPIRB \n\n2) 1 VHF RT DSC DSC watch receiver - 1 or 2 SART-1 NAVTEX or 1 EGC receiver-2 or 3 VHF portable - 1 EPIRB  \n\n3) 1 VHF.RT DSC DSC watch receiver - 1 or 3 2 SART-1 NAVTEX or 1 EGC receiver- 2 or 3 VHF portable \n\n4) 1VHF RT-1 or 2 SARTI NAVTEX or 1 4 EGC receiver- 2 or 3 VHF portable - 1 EPIRB",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "The best way to prevent stowaways from boarding your ship is to: \n\n1) Conduct routine, but irregular searches of the ship. \n\n2) Conduct a Nominated Officers search, \n\n3) Seal spaces that are not in use while in port, and perform a search of the ship before leaving. \n\n4) Search the ship when you arrive at port and again just after leaving",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "One wishes to have a telephone conversation with a person whose name is known. This is what is called: \n\n1) A call to a known person \n\n2) A collect call  \n\n3) A direct call \n\n4) A personal call",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "According to Rule 35 of the International Regulations for Preventing Collisions what sound signal is made by a vessel not under command when in or near an area of restricted visibility? \n\n1) One prolonged blast, followed by two short blasts, at intervals of not more than two minutes \n\n2) Two prolonged blasts, followed by one short blast, at intervals of not more than two minutes \n\n3) One prolonged blast, followed by two short blasts, at intervals of not more than one minute \n\n4) One prolonged blast at intervals at not more than two minutes",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Poster or signs shall be provided on or in the vicinity of survival craft and their launching controls. Which one of the following requirements has to be included? \n\n1) Give information on survival craft speed and seaworthiness \n\n2) Give relevant instructions and warnings  \n\n3) Give an overview of location of all lifesaving appliances \n\n4) Give information on survival 4 craft capacity",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Who is responsible for completing the DoS on behalf of the ship? \n\n1) Chief Engineer \n\n2) Company Security Officer  \n\n3) Ship Security Officer \n\n4) Chief Officer",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Your vessel is towing an unmanned barge and restricted in its ability to manoeuvre. The total length of the tow is 800 metres. What daylight signals are required by the International Regulations for Preventing Collisions at Sea? \n\n1) Three shapes shall be displayed on the tug, where they can best be seen, in a vertical line, the upper and lower being balls and the middle one a cylinder. The signal flag (T) shall also be flown on the tug. A diamond shall be displayed aft on the tow \n\n2) Three shapes shall be displayed forward on the tug, in a vertical line, the upper and lower being balls and the middle one a diamond  \n\n3) A diamond shape, where it can best be seen, on the tug only. Three shapes shall also be displayed, being three balls in a vertical line \n\n4) A diamond shape, where it can best be seen shall be displayed on the tug and the tow. Three shapes shall also be displayed in a vertical line, the upper and lower being balls and the middle one a diamond",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "On a conventional rudder, how much lift force remains if the rudder-angle is decreased to 20 degrees, from an initial 35 degrees? \n\n1) About 80% \n\n2) About 50% \n\n3) About 30% \n\n4) About 10%",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "What rules and regulations are regulating the watch keeping routines in the engine room? \n\n1) International Standard for Training and 2 Watch keeping (STCW) \n\n2) Both STCW and Class rules \n\n3) SOLAS \n\n4) Class Rules",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "How is a 'sidelight' described in rule 21 of the International Regulations for Preventing Collisions at Sea? \n\n1) A red, green or yellow lantern, showing an unbroken light over an arc of 112.5 degrees\n\n2) A red light or a green light, with a minimum range, in a vessel of 50 metres or more, of miles. In a vessel of 10 metres or more but less than 50 metres in length, a range of 1 mile  \n\n3) A green light on the starboard side and red light on the port side, showing an unbroken light over an arc of 112.5 degree, from right ahead to 22.5 degrees abaft the beam on the respective side \n\n4) A green light on the starboard side and red light on the port side, showing an unbroken light over an arc of 135 degrees, from right ahead to 22.5 degrees abaft the beam on the respective side",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "On area A1 the function (Reception of shore to ship distress alerts) is mainly based on: \n\n1) the use of SART transponders \n\n2) the use of SARSAT COSPAS Epirbs \n\n3) the use of MF DSC \n\n4) the use of VHF DSC",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "What is the status of the rules of the SOLAS convention? \n\n1) Mandatory.\n\n2) Supplementary to classification rules. \n\n3) Must be regarded as guidelines. \n\n4) Should be consulted when the vessel is in distress",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Part way through a profiling interview with a supplier, the package the individual is carrying arouses your suspicion. What do you do? \n\n1) Call for help on the radio.\n\n2) Discreetly inform someone of your suspicions so he or she can get assistance. \n\n3) Confront the individual and demand that he open the package. \n\n4) Take the package and open it",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Which of these statements about drug smugglers modes of operating is true? \n\n1) Drugs hidden by individual entrepreneurs are usually difficult to detect. \n\n2) An organized conspiracy usually smuggles a small amount of drugs \n\n3) Drugs smuggled by an organized conspiracy are usually concealed in a primary ship system such as the engine room or in a tank, void or compartment. \n\n4) Individual entrepreneurs usually smuggle large quantibes of drugs.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Testing a SART is permitted: \n\n1) Only in a port or harbour \n\n2) Only at sea, outside territorial waters  \n\n3) Only in the workshop \n\n4) At sea, outside territorial waters, and in port or harbour",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Under GMDSS which VHF channel is used for Digital Selective Calling (DSC)? \n\n1) Ch. 70 \n\n2) Ch. 13  \n\n3) Ch.06 \n\n4) Ch. 16",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "The mode J2B is used: \n\n1) In public broadcasting \n\n2) For radiotelex-traffic in the MF/HF band between the ship and shore stations \n\n3) For telephone traffic in the MF/HF bands between ship and shore stations \n\n4) For urgent message transmitting and receiving",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Your ship security plan must include procedures for responding to security threats, auditing security activities and interfacing with the port facility \n\n1) \n\n2)  \n\n3) TRUE \n\n4) FALSE",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Your vessel is power-driven and making way in open water. This vessel is sighted wide on the port bow. It's bearing is opening, but its distance is closing rapidly. Which of the following is a correct assessment of the situation and the action to be taken? \n\n1) Risk of collision is deemed to exist and I will make a broad alteration of course to starboard, sounding one short baat I will re assess the situation when the alteration is carried out \n\n2) Risk of collision is a possibility. I will maintain my course and speed for now, but be prepared for an alteration of course to port if the CPA seems to be less than 0.2nm as we draw closer \n\n3) Risk of collision is deemed not to to exist. However, to be sure of a safe passing distance, I will reduce my speed to allow the other vessel to pass ahead \n\n4) Risk of collision is deemed not to exist and I will maintain my course and speed. I will continue to monitor the situation",
                           "https://t.me/picturesforbo/90", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "What IMO conventions take care of the human safety at sea? \n\n1) It is the SOLAS conventions that take care of the human safety at sea \n\n2) There isn't any conventions that take care of the human safety at sea \n\n3) It is the STCW 78/95 that take care of the human safety at sea \n\n4) It is the MARPOL conventions that take 4 care of the human safety at sea",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "What do you do after receiving a VHF DSC DISTRESS call? \n\n1) You set watch on channel 13 \n\n2) You set watch on VHF channel 16 \n\n3) You send immediatly a DSC DISTRESS RELAY call\n\n4) You send immediately a DSC DISTRESS ACKNOWLEDGEMENT call",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "The receipt of a distress alert is to be pronounced as followed: \n\n1) Mayday (ix)/distress aleert / own ship call sign \n\n2) Mayday (Ix)/this is/ own call-sign (3x) received mayday \n\n3) Mayday (Ix), call-sign of ship in distress (3x)/this is / own call-sign (3x)/received mayday \n\n4) Mayday (3x)/thisis/ own call-sign (1x)/  received mayday/call-sign of ship in distress (1x)",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Which method illustrated is the proven way to get two vessels in open water safely alongside each other for a ship to ship transfer operation? Note that not all the vessels are moving. \n\n1) When the larger vessel is at anchor, fig. 2\n\n2) When the smaller vessel is at anchor, fig. 3\n\n3) When the larger vessel is stopped and drifting in the water, fig. 4 \n\n4) When both vessels are making way, fig. 1",
                           "https://t.me/picturesforbo/91", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Which IMO convention takes care of the human safety at sea ?\n\n1) The SOLAS convention \n\n2) there isn't any conventions that take care of the human safety at sea \n\n3) the MARPOL convention\n\n4) the MARPOL convention",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "If one wishes to make a collect call from a vessel to a shore subscriber, one must: \n\n1) Inform the telephone number on whom to charge the call \n\n2) Request for a collect call \n\n3) Request for telephone message stating name, address and telephone number \n\n4) Request for a personal cal",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "MARPOL-Annex IV. Your ship has in operation an approved sewage treatment plant certified by the Administration. During discharge, while vessel is awaiting pilot off Cape Henry, USA, the surrounding water is discoloured. What kind of action would be appropriate to take? \n\n1) Continue discharge since Annex IV of MARPOL is internationally not yet in force. \n\n2) Continue discharge since the treatment plant is of an approved type.\n\n3) Stop discharge. \n\n4) Reduce discharge rate in order to have less discolouration of surrounding wale",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "A (Standard Format for Search and Rescue Situation Reports) (SITREPs) should be used by vessels in distress. The SITREP can be compiled as a short form (urgent essential details). Which of the following information shall be included when using the (short form)? \n\n1) Position. \n\n2) Oil spill possibility. \n\n3) Cargo information. \n\n4) Weather on-scene.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Which VHF channel should be used for intership navigation safety communications? \n\n1) Ch. 13 \n\n2) Ch. 16 \n\n3) Ch. 12 \n\n4) Ch.06",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Which VHF channel should be used for intership navigation safety communications? \n\n1) Ch. 13 \n\n2) Ch. 16 \n\n3) Ch. 12 \n\n4) Ch.06",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "MARPOL-Annex I. Your vessel sailed from Bahrain heading for Singapore. 2 days after departure, you would like to empty your machinery space bilges. What will be the correct procedures in this connection? \n\n1) Call the bridge and request for position and permission to discharge directly overboard. \n\n2) Wait till after darkness and discharge in most convenient way. \n\n3) Call the bridge and request for position and permission to discharge overboard through oily water separating and filtering equipment. \n\n4) Discharge overboard through oily-water separating and filtering equipment without calling the bridge.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "When a vessel is undertaking a long canal transit with locks and lots of activity, what management issues should the Master consider? \n\n1) Fully manned engine room throughout the canal transit \n\n2) Suitable crew available for lock transits \n\n3) Lack of sleep and fatigue of 2 bridge officers \n\n4) All of these answers",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "For a DSC-connection (no 'distress alert') with another vessel the following frequencies are used: \n\n1) TX: 2177.0 kHz RX: 2177.0 kHz \n\n2) Tx: 2187.5 kHz RX: 2182.0 kHz \n\n3) Tx: 2187.5 kHz RX: 2182.0 kHz \n\n4) TX: 2189.5 kHz RX: 21895kHz",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "A rocket parachute flare reaches an altitude of \n\n1) not less than 40m \n\n2) not less than 300m \n\n3) not less than 180m \n\n4) not less than 450m",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Your vessel has been involved in a collision, which has resulted in a heavy oil leakage. Who should be called to handle pollution claims and damages? \n\n1) Flag state representative \n\n2) The Classification Society's representative.\n\n3) The P & I Club's nearest representative. \n\n4) The Leading Hull Underwriter's nearest Average Agent ",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "What action should be taken by the Officer of the Watch if someone reports a fire to them? \n\n1) Send the bridge look-out down to investigate \n\n2) Call the Master \n\n3) Call the MasterThe P & I Club's nearest representative. \n\n4) Sound the Fire Alarm ",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Your vessel has been involved in a collision, and at first opportunity a lot of people from outsides parties are asking questions. What shall you tell them? \n\n1) Do not reply to any questions from outside parties, except the Solicitor appointed by your company. \n\n2) To make sure that all parties are informed about the facts, show them the extracts of the log-book. \n\n3) You shall only tell them the truth and nothing but the truth. \n\n4) Do not tell anybody anything, except representatives from the main newspapers. radio and TV. Remember, the people have the right to know. ",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "When reasonable and practicable, how often shall rescue boats be launched with their assigned crew aboard and manoeuvred in the water? \n\n1) Every week \n\n2) Every month \n\n3) Every six months \n\n4) Every two weeks",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "A MF/HF-DSC multi-frequency call attempt may: \n\n1) Be repeated after 15 minutes \n\n2) Be repeated after 1 to 1.5 minutes \n\n3) Be repeated after 3.5 to 4.5 minutes \n\n4) Not be repeated",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "A large vessel is proceeding under its own power in a narrow channel, assisted by a tug. Where should the tug be connected to best assist the ship maintain steerageway? \n\n1) Standing-by-ready for use anywhere, as required \n\n2) Made fast an a line through the centre lead forward  \n\n3) Pushing alongside - either side \n\n4) Made fast on a line through the centre lead aft",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "If one requires medical advice by means of an Inmarsat-C terminal one should use the following address: \n\n1) 32 \n\n2) Radiomedical \n\n3) Sick Seaman \n\n4) MED",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "A deep draught vessel sailing in a very narrow channel can develop a sudden sheer as it slows down. What could be the cause of this? \n\n1) The vessel stopping shifts the pivot point forward and creates a turning moment and results in the ship swinging towards the bank. \n\n2) The large volume of water dragged behind the vessel continues to move forward and cause a strong turning moment on the stern of the vessel \n\n3) The hydrodynamic interaction effects from ? the banks of the shallow water channel acts on the stern causing the vessel to sheer strongly  \n\n4) The shallow water reduces the A effectiveness of the rudder and when the vessel stops any applied rudder will become suddenly more effective.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Operator connected R/T calls are charged \n\n1) On the basis of a six second minimum charge with six second incremental steps \n\n2) On the basis of a six second minimum charge with one second incremental steps \n\n3) On the basis of a three minute minimum charge with one minute incremental steps\n\n4) On the basis of a one minute minimum charge with one minute incremental steps",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "For how long time should a COSPAS-SARSAT epirb be able to operate on its batteries? \n\n1) 12 hours \n\n2) 96 hours \n\n3) 24 hours \n\n4) 48 hours",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "In US waters (Oil Pollution Act of 1990) was activated in August 193. What is the main issue for the introduction of the act? \n\n1) To prevent oil spills in US waters? \n\n2) To encourage owners to build double hull vessels for trading US waters? \n\n3) To enforce owners to use equipment of higher standards that those of today? \n\n4) To improve safety measures onboard?",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "To get priority with radio-communication, one must notify the coast-station that the call is: \n\n1) A collect call \n\n2) An urgent call \n\n3) A personal call \n\n4) A priority call ",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "What mode is used for broadcast an MF/HF- DSC message: \n\n1) H3E \n\n2) J3E \n\n3) J2B/FIB  \n\n4) G3E",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Notification logging procedures (OPA-90) \n\n1) Only initial reports to be logged \n\n2) Only communication with USCG \n\n3) Only verbal reports for documentation \n\n4) Every report or message must be logged including time and date",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "The Urgency Message from a ship is used to notify other traffic of a situation where the ship is not in imminent danger, but where the development of the situation is uncertain and may need assistance in the near future. What is the telephony urgency message like? \n\n1) PAN-PAN \n\n2) RESCUE-RESCUE \n\n3) SECURITY  \n\n4) MAYDAY",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Which of these statements about profiling is correct? \n\n1) Pay less attention to body language and behaviour and more attention to answers to questions. \n\n2) Check the ID of all visitors and some crew prior to boarding \n\n3) Verify that answers to questions match up with what's already known about the person being questioned.  \n\n4) Use only open-ended questions.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Assign men to search men and women to search women unless a device such as a metal detector is used. \n\n1) FALSE \n\n2). \n\n3). \n\n4)TRUE",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "When a message is sent by the Inmarsat-C installation to an Internet e-mail address, the land charge is: \n\n1) Dependent on the 'chargeband \n\n2) Independent of the destination \n\n3) Dependent on the type of terminal used \n\n4) Dependent on the destination",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Under ISM, what is a (non-conformity)? \n\n1) A safety officer not being nominated for the vessel \n\n2) Official log book entries not being completed correctly \n\n3) An observed situation where objective evidence indicates the non-fulfilment of a specified requirement \n\n4) The wearing of non-standard Personal protective equipment",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "On board a DSC-call is to be made in case of an OBS. Choose the category: \n\n1) Ship's business \n\n2) Safety \n\n3) Urgency \n\n4) Routine",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "A Cospas-Sarsat EPIRB can be used in: \n\n1) All sea-areas (Al to A4) \n\n2) Only in the sea-areas A2 and A3 \n\n3) Only in sea-area A4 \n\n4) Only in the sea-areas Al, A2 and A3",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "How does the International Regulations for Preventing Collisions define a 'vessel restricted in her ability to manoeuvre'? \n\n1) A vessel which because of her draught in relation to the available depth of navigable water is restricted in her ability to deviate from her course and keep out of the way of another vessel \n\n2) A vessel which from the nature of her work is restricted in her ability to manoeuvre as required by the Rules and is therefore unable to keep out of the way of another vessel \n\n3) A vessel engaged in underwater work, such as the laying, picking up or servicing of a pipeline, or which is in support of diving operations, performing dredging and mine clearance or a deploying or recovering a pilot \n\n4) A vessel which through some exceptional circumstance is unable to manoeuvre as required by the Rules and is therefore unable to keep out of the way of another vessel",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Give the meaning of the following symbol \n\n1) Survival craft distress pyrotechnic signals \n\n2) EPIRB \n\n3) Radar transponder \n\n4) Rocket parachute flares",
                           "https://t.me/picturesforbo/92", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "A small vessel with a right handed propeller and no thruster is approaching a berth with an onshore wind. What is the best way to have a controlled berthing? \n\n1) Stop the engine and let the vessel momentum and the wind drop the vessel onto the berth \n\n2) Reduce speed by going full astern on the engines \n\n3) Full starboard rudder and stop engines \n\n4) Dredge a forward anchor, working the engine and rudder against it to keep the stern up",
                           "https://t.me/picturesforbo/93", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Small oil spills on deck can be kept from going overboard by doing what? \n\n1) Plugging the scuppers \n\n2) Driving wooden plugs into the vents \n\n3) Full starboard rudder and stop engines \n\n4) Plugging the sounding pipes",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "How will you start a cancelling message after you send by mistake a distress call on your VHF DSC equipment \n\n1) MAYDAY All Stations - This is SAINT-ROMAIN \n\n2) All Stations - This is SAINT-ROMAIN \n\n3) SECURITE All Stations. This is SAINT-ROMAIN \n\n4) PAN PAN-All Stations. This is SAINT ROMAIN",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "The accuracy of an Inmarsat-E positioning- system is: \n\n1) 5 miles \n\n2) 20 meters \n\n3) 200 meters \n\n4) 20 miles",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "The whip-antenna of the MF transceiver was lost in bad weather. The MF-transceiver can be used again: \n\n1) Only if the whip antenna is replaced by another whip-antenna of the same length \n\n2) If instead of the whip-antenna, another whip-antenna such as the spare VHF antenna is connected \n\n3) If the whip-antenna is replaced by a Sat Cantenna \n\n4) If the whip-antenna is replaced by an antenna of about the same length as the original one",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "On-board training in the use of davit- launched liferafts (including inflation and lowering whenever practicable) must take place \n\n1) every 4 months \n\n2) every 2 months \n\n3) every month \n\n4) every 3 months",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Your vessel is in restricted visibility and you hear this signal. What type of vessel does it come from and what additional information does the signal provide? \n\n1) A vessel aground, more than 100 metres in length. The additional signal indicates which side the clear water lies on\n\n2) A vessel at anchor, more than 100 metres in length. She is sounding the additional signal to give warning of her position \n\n3) A vessel at anchor, more than 100 metres in length. The additional signal indicates that her cable extends at least 25 metres from her bow \n\n4) A vessel at anchor, less than 100 metres 4 in length. She is sounding the additional signal top give warning of her position",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "On area A1 the function  (Reception of shore to ship distress alerts) is mainly based on: \n\n1) The use of SARSAT COSPAS Epirbs \n\n2) The use of SART transponders \n\n3) The use of VHF DSC \n\n4) The use of MF DSC",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Referring to the SOLAS convention, how often should a crew member on a cargo ship participate in one abandon ship drill and one fire drill? \n\n1) This is only required when he joins the ship \n\n2) Weekly \n\n3) Every second week\n\n4) Monthly",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Which information should be included in your search plan? \n1)Areas to be searched and personnel to be involved in the search. \n\n2)Areas to be searched. \n\n3) Personnel to be involved in the search \n\n4) Known hiding spots to be searched.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "MARPOL-Annex IV. Prevention of Pollution by Sewage from ships. What do you understand by the word (Sewage)? \n\n1) Waste from galley. \n\n2) Drainage/waste from toilets/urinals. \n\n3) Mixture of sea water/oil.\n\n4) Waste from synthetic materials.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Which type of call will be sent by a ship sighting another ship in distress which is not itself in position to transmit a distress alert? \n\n1) Urgent call \n\n2) Distress call \n\n3) Distress relay call\n\n4) Safety call",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "What sound signal can be made when nearing a bend in a river, with the view around the bend obscured by an intervening obstruction? \n\n1) Two short blasts \n\n2) One short blast \n\n3) Two prolonged blasts \n\n4) One prolonged blast",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "How many annexes do we find in MARPOL and what is the content of annex 1? \n\n1) We find 6 annexes in MARPOL and annex 1 is the regulations for the prevention of pollution by oil \n\n2) We find 5 annexes in MARPOL and annex 1 is the regulations for the prevention of pollution by sewage \n\n3) We find 4 annexes in MARPOL and annex  I regulations for the prevention of pollution by garbage \n\n4) We find I annexes in MARPOL and annex I regulations for the prevention of pollution by chemicals",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "The type-indication of the radio set is mentioned in: \n\n1) The survey of equipment \n\n2) The safety certificate \n\n3) Registry certificate \n\n4) The equipment appendix",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "A Ship Security Assessment is integral to the creation of your ship's security plan. \n\n1) \n\n2)FALSE \n\n3)TRUE  \n\n4)",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "If whistles are fitted on a vessel at a distance apart of more than 100 metres, will manoeuvring and warning signals, as defined by rule 34 of the International regulations for Preventing Collisions at Sea, be given on one or both whistles? \n\n1) Manoeuvring signals will be given only on the forward whistle; warning signals will be given on both whistles simultaneously \n\n2) They shall be given on both whistles simultaneously \n\n3) They shall first be given on the forward whistle, followed by the after whistle, with a 5 second inetrval in between  \n\n4) They shall be given on one whistle only",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "Give the meaning of the following symbol \n\n1) EPIRB \n\n2) Survival craft portable radio \n\n3) Survival craft distress pyrotechnic signals  \n\n4) Rocket parachute flore",
                           "https://t.me/picturesforbo/94", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "The word RADIO is spelled conform the international phonetic alphabet: \n\n1) Romeo, Alpha, Delta, India, October \n\n2) Romeo, Alfa, Delta, India, Oscar \n\n3) Radio, Alfa, Delta, India, Oscar  \n\n4) Romeo, Atlanta, Delta, India, October",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "Who should inspect the rigging of a pilot ladder and accompany a pilot on deck at embarkation/disembarkation? \n\n1) An experienced AB \n\n2) The Sen.Off.Deck only \n\n3) A responsible Officer  \n\n4) The Bosun",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Would the indicated ground speed be suitable when berthing a large vessel? \n\n1) The approach speed is essential to maintain steerage when coming alongside \n\n2) The indicated speed would be a normal speed approaching a berth \n\n3) The approach speed is way too fast, even for a vessel in ballast.  \n\n4) The speed requirements are decided by the pilot and should not be the concern of the OOW.",
                           "https://t.me/picturesforbo/96", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "The compulsory testing of a prescribed EPIRB is to be done: \n\n1) Once a year \n\n2) Once a week \n\n3) Once in 4 years  \n\n4) Once a month",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "You are on a power-driven vessel underway in open water. This vessel is sighted directly ahead. The distance is closing slowly. What action will you take under the International Collision Regulations and why? \n\n1) I will keep out of her way. I am the overtaking vessel and am obliged to keep clear under rule 13 \n\n2) The vessel is on a steady bearing and the distance is closing. I will therefore take avoiding action, altering course to starboard and sounding one short blast under rules 14 and 16  \n\n3)This is a vessel engaged in towing and I am seeing the stern light of the tow. The tug is not however showing any lights indicating she is restricted in her ability to manoeuvre. I will however display good seamanship and keep out of her way \n\n4) I will maintain my course and speed. The other vessel is being overtaken and is therefore obliged to keep out of the way by rule 13",
                           "https://t.me/picturesforbo/97", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Why is it important to make weekly/routine rounds in the accomodation areas? \n\n1) It is a requirement as per flag state \n\n2) To ensure that cabins and common spaces are maintained in a clean, safe and hygienic condition \n\n3) To check for alcohol in cabins \n\n4) To search for any contraband goods hidden on board",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "In Which publication will you find the working frequencies of coast stations? \n\n1) The ITU List of Ship Stations \n\n2) The ITU List of Call signs and Numerical Identities of Stations used by the maritime mobile and anime mobile-satelite services \n\n3) The ITU List of coast stations \n\n4) The ITU List of Ship Stations",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Satellites which receive the 406 MHz Cospas-Sarsat EPIRB are: \n\n1) Capable to determine position only in duy time  \n\n2) Not capable to determine the position of the EPIRB \n\n3) Only capable to determine the position of the EPIRB in certa certain curcumstances \n\n4) Capable to determine the position of the EPIRB",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "What percentage of the ship's stores are required to be inspected at Security Level 3? \n\n1) 100% of the ship's stores are required to be inspected at Security Level 3.  \n\n2) 50-80% of the ship's stores are required to be inspected at Security Level 3. \n\n3)5-20% of the ship's stores are required to be inspected at Security Level 3. \n\n4) 25-50% of the ship's stores are required to be inspected at Security Level 3",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "You want to send a DSC-call in connection with a shore telephone-call. You must choose: \n\n1) Distress  \n\n2) Routine \n\n3) Urgency \n\n4) Safety",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "In the situation illustrated with a vessel turning a bend in a narrow river, what outside forces effect the handling of the vessel? \n\n1) The only force from the outside on the vessel will be bottom effect, because the river is likely to be quite shallow  \n\n2) None, as the river flow will be fairly uniform guiding the vessel \n\n3) Bow and stern attraction/rejection force caused by the closeness of the river sides \n\n4)  The only likely outside force effecting the vessel will be from wind and river flow",
                           "https://t.me/picturesforbo/98", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "When manoeuvring a conventional ship, if the engine is stopped with the rudder hard over what happens to the rudder turning force? \n\n1) Anything might happen as it depends upon the type of specialiseradder fitted \n\n2) It stays the same as the rudder angle is unchanged \n\n3) It may increase due to a better laminar flow on the rudder \n4) It is reduced because of the reduced water acting on the rudder",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "The muster list must be prepared: \n\n1) At any moment before the ship proceeds to sea \n\n2) at least 2 hours before the ship proceeds to sea \n\n3) at least 1 hour before the ship proceeds to sea \n\n4) at least 2 hours after the ship has proceeded to sea",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "Which of the following channels and modes should be used when initiating a distress alert transmission? \n\n1) Channel 6 DSC \n\n2) Channel 70 DSC \n\n3) Channel 6 Radiotelephony \n\n4) Channel 13 Radiotelephony and channel 16 DSC",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "How is a Safety Management Certificate obtained? \n\n1) Vessel is surveyed by MCA and 2 certificate issued \n\n2) RSS issue SMC with Register \n\n3) Ship owner has Document of Compliance issued, and vessel is assessed and holds all statutory certificates \n\n4) Ship owner is authorised to carry out internal audits and issue SMC",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Which of the following channels and modes should be used when initiating a distress alert transmission? \n\n1) Distress call \n\n2) Urgency call \n\n3) Individual call \n\n4) Safety call",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        await add_question(test_id,
                           "The analyses of the smoke produced by a fire, may give an interpretation of that fire. Which are the factors we should take into account? \n\n1) Opacity, amount and colour \n\n2) Colour only \n\n3) Amount and opacity only \n\n4) There is no possible interpretation of a fire according to the smoke",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)
        await add_question(test_id,
                           "On area A3 the function ( Transmission and reception of on scene communications) is mainly based on:  \n\n1) The use of HF DSC \n\n2) The use of MF and/or VHF R/T \n\n3) The use of MF and/or HF R/T \n\n4) The use of DSC and/or INMARSAT C",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)
        await add_question(test_id,
                           "When a Master takes the leadership in approaching a problem, Must his first action be a decision that will directly solve the problem? \n\n1) Yes, take full controll. Do not delegate to other officers, to avoid mistake. \n\n2) Yes, with his experience, it is most likely that he has the best solution \n\n3) Not necessary, he shall use all available resources. He should resist the temptation to step in and do it all by himself \n\n3) No, he should obsery the situation, and let the other senior officers solve the situation.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)
        await add_question(test_id,
                           "Which one of the following items has to be included in an abandon ship drill according to SOLAS regulations? \n\n1) Manoeuvring the lifeboat in the water. \n\n2) Launching and recovery of a survival craft. \n\n3) Starting and operating radio life-saving appliances. \n\n4) Checking that life-jackets are correctly donned.",
                           "https://t.me/picturesforbo/196", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)
        # Добавьте другие вызовы add_question для добавления остальных вопросов к этому тесту

        print(f"Вопросы для теста '{name}' успешно добавлены.")

    except Exception as e:
        print(f"Ошибка при добавлении теста {name} или вопросов к нему: {e}\n{traceback.format_exc()}")


async def main():
    await add_specific_test_questions()
    print("Данные для специфического теста успешно обработаны.")


if __name__ == "__main__":
    asyncio.run(main())
