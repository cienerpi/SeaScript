import asyncio
import traceback
from database_manager import add_test, add_question


async def add_specific_test_questions():
    # Определяем название и отдел только для интересующего нас теста
    name = "CES 6 Slow Speed (Management)"
    department = "mechanics"

    try:
        test_id = await add_test(name, department)


        await add_question(test_id,
                           "The machinery detail plate is missing from a large electric motor and the weight is unknown. As part of a routine maintenance check the motor has to be lifted to access some other equipment. Which of the given options is the correct action that should be taken? \n\n1) As it is only a routine maintenance and not a breakdown then postpone the task until full details of the motor can be obtained. \n\n2) Try and lift it with the engine room crane as it is designed to lift the heaviest components in the engine. \n\n3) Use the biggest chain blocks and strops available and carry out a trial lift. \n\n4) Estimate the weight of the motor and select a chain block and strop with a safe working load of 1.5 times the calculated load.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "A positive displacement, rotary type, volumetric flow meter reads low with an error reading of 1% when used to measure flow of heavy oil and 2.5% when used to measure the flow of diesel oil. From the options given select the most likely cause of this difference in error? \n\n1) \n\n2) The meter is worn internally.The low lubricity of the diesel oil is increasing the friction in the rotating element and slowing the rotor down.  \n\n3) The higher viscosity of the heavy oil is slowing down the rotary element in the meter. \n\n4) The lower mass of diesel oil results in a lower reading.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Electric arc welding is to be carried out in the machinery spaces other than the workshop. Which of the alternatives below would be the preferred method for the connection of the 'return' cable to the welding set? \n\n1) Weld a stud bolt close to the work piece and connect the return cable to this. \n\n2) Use a 'go and return' system with the return cable connected directly from the welding set to the work piece if possible. \n\n3) Have a short length of cable permanently connected to the ships structure close to the welding set. \n\n4) Move the welding set to the welding site.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "What would the results of a TAN test, carried out on lubricating oil samples from a diesel engine, indicate? \n\n1) A measure of the remaining alkalinity in the lubricating oil. \n\n2) A measure of the inorganic acids in the lubricating oil. \n\n3) A measure of the of organic and inorganic acids in the lubricating oil. \n\n4) A measure of the organic acids in the lubricating oil.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "A 2 term controller is used to control the fuel oil temperature for a thermal oil system used for heating services. The control is very unstable with the measured value hunting constantly. Select the most probable cause of this problem from the options given. \n\n1) Proportional band width is set too wide. \n\n2) Proportional band width is set too narrow. \n\n3) Integral action reset time is set too slow. \n\n4) Integral action reset time is set too fast.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "A 3-phase cage rotor induction motor requires protection by a time delay overload trip. What is the reason for this? \n\n1) It will tolerate fault conditions during start up. \n\n2) Fuses act too quickly. \n\n3) Fuses act too slowly. \n\n4) It will allow for inrush current or motor specific faults.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Prior to the lunch break, the Engineer on Duty observes that the operating generator set has an output of 90%. With regard to operation of the generator, what is the - most important - assumption(s) for him to check before switching to UMS-mode? \n\n1) All parameters as listed under the other alternatives. \n\n2) That a secondary auxiliary set is switched to automatic standby mode. \n\n3) That all operating parameters of the generator set in operation are normal (e.g. exhaust temp, lubeoil pressure, cooling water temperature etc.) \n\n4) Visually checking the auxiliary engine that there are no leaks or other obvious operating failures.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Hand flares and buoyant smoke signals can continue to burn or emit smoke after having been immersed for a period of 10s. What is the reason for this? \n\n1) Right if the immersion depth is smaller than 100 mm. \n\n2) Right. \n\n3) Right if the immersion depth is more than 1m. \n\n4) Wrong.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Select the option which correctly completes the following statement. 'Prior to allowing work to proceed in an onboard space testing the atmosphere should be carried out... \n\n1) ...only if the space has been used to carry any cargo or contains any cargo related equipment. \n\n2) ...for any space with limited access or non-continuous ventilation or is suspected of having a hazardous atmosphere. \n\n3) ...only if the space has a watertight door or watertight access opening. \n\n4) ...only if the space has contained liquid oil at some point.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "What type of dynamic forces may cause indent in plating on forecastle deck and main deck in way of pillars inside forecastle? \n\n1) Pressure forces caused by green water on deck. \n\n2) Forces created by waves on the forecastle. \n\n3) Slamming in way of flat bottom forward of light draught. \n\n4) Impact pressure forces in way of abrupt or flared bow.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "What should be the status of the suction and discharge valves when starting a centrifugal pump? \n\n1) Suction valve closed and discharge valve open. \n\n2) Suction valve open and discharge valve closed. \n\n3) Both valves open. \n\n4) Both valves closed.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "The continuity resistance of a 100m long X 25 sq. mm cable (rated at 100A) is to be checked. Which of the following results would you anticipate? \n\n1) between 0.1micro ohm and 1.0 micro ohm. \n\n2) greater than 1 M ohms. \n\n3) between 0.1 and 1.0 ohm. \n\n4) between 0.1 and 1.0 M ohm.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "The Muster List shall show the duties assigned to members of the crew. Which of the following duties shall be included according to present regulations? \n\n1) Special duties assigned with respect to the use of pyrotechnics. \n\n2) Preparation of immersion suits for passengers. \n\n3) Operation of the vessel's propulsion system. \n\n4) Manning of fire parties assigned to deal with fires.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "A portable oxygen analyser for use onboard ship is of the paramagnetic sensing element type. It is being used to test the atmosphere of a space onboard ship but starts to give erratic readings. There is no obvious indication as to why this is happening. Select from the options given the most likely cause of this problem. \n\n1) The sampling filter is partially blocked giving rise to wide pressure variations in the sampling chamber. \n\n2) The battery power is low. \n\n3) Nitrogen gas is present in the atmosphere. \n\n4) The sampling filter is blocked preventing gas from entering the sampling chamber.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "When reasonable and practicable, how often shall rescue boats be launched with their assigned crew aboard and manoeuvred in the water? \n\n1) Every two weeks. \n\n2) Every week. \n\n3) Every six months. \n\n4) Every month.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "In case of a pollution in US waters, who shall notify the cleaning up contractor (OPA-90)? \n\n1) The shipowner.  \n\n2) Qualified Individual. \n\n3) Emergency response team. \n\n4) The Master.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Many large, slow speed diesel engines have direct oil cooling of the piston crowns provided. An automatic slow down and alarm are sometimes fitted to protect against failure of this system. Which parameter is usually used to initiate this slow down? \n\n1) Low oil pressure in the piston crown cooling space. \n\n2) Low pressure in the cooling oil return line. \n\n3) Low flow or no flow in the cooling oil return line. \n\n4) High temperature of the piston crown.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "When starting air is applied to a diesel engine the engine fails to turn over but is seen to oscillate back and forth. What is the most likely cause of this problem? \n\n1) An interlock is blocking the air to the starting air distributor. \n\n2) Starting air pressure is too low. \n\n3) The automatic valve has failed to open. \n\n4) One or more cylinder air start valves are stuck open.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Prior to bunkering operations it is necessary to check the quantity of fuel remaining onboard and that there is sufficient room for the fuel that is to be loaded. What is the best method to use to establish this? \n\n1) Do a complete sounding of all fuel bunker tanks. \n\n2) Take a full set of readings from remote content gauges. \n\n3) Sound the tanks which you think might still contain some fuel. \n\n4) Use the latest figures from the fuel record book.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The temperature control for the central cooling system low temperature circuit has failed and a new 3 term controller is to be fitted. Which of the given options would be the correct method of setting up the controller? \n\n1) Set the integral action first. \n\n2) Set the proportional action first. \n\n3) Set the derivative action first. \n\n4) All three actions should be set simultaneously.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "The Master is responsible that all crew participate in monthly emergency drills. If 25% of the crew - or more - has not participated in such drill during the last month, what is the time limit to conduct such a drill after the vessel has left a port? \n\n1) Within 30 hrs. \n\n2) Within 48 hrs. \n\n3) Within 24 hrs. \n\n4) Within 12 hrs.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Which of the following options is the most likely cause of high exhaust gas temperatures in all cylinders of a diesel engine? \n\n1) Water in the fuel supply. \n\n2) Faulty high pressure fuel pump on one of the cylinders. \n\n3) Worn or broken piston rings. \n\n4) Partial blockage in the exhaust gas system.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "A High Breaking Capacity fuse found in a Main High Voltage Switchboard will typically have fault level rating of? \n\n1) 40 kA \n\n2) 40A \n\n3) 4000A \n\n4) 400A",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Three earth lamps indicate (under no test mode) - bright - bright - dark. Which of the following is indicated by this condition? \n\n1) Two phases are good and one has a partial fault to earth \n\n2) A failed lamp \n\n3) Two phases are good and one has a hard fault to earth \n\n4) Two phases have a partial fault to earth and one is good",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "You are in charge of a night bunkering operation. The delivery rate from the supplier is high and you are filling six tanks simultaneously. You lose track of the progress of the operation and feel that you are losing control of the situation. What action should you take? \n\n1) Prepare yourself and the crew for an overflow. \n\n2) Request a reduction in the delivery rate to try and gain some time. \n\n3) Stop bunkering, and establish facts, before bunkering is resumed  \n\n4) Open more tanks to slow down the filling rate of individual tanks.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "During inspection of a cylinder liner for a large, slow speed diesel engine it is found to be worn in a cloverleaf pattern. The greatest points of wear are found to be in way of the cylinder lubricator holes. From the options given, what is the most likely cause of this type of wear pattern? \n\n1) Fuel impingement on the liner due to faulty fuel injector nozzle. \n\n2) Excessive cooling of the cylinder liner at low load operation. \n\n3) Insufficient cylinder lubricating oil being supplied. \n\n4) Cylinder lubricant has too high an alkalinity for the sulphur content of the fuel.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "What type of lubricating oil is generally used for cylinder lubrication on a large, 2-stroke diesel, main propulsion engine operating on heavy fuel oil? \n\n1) Mineral based oil with high alkalinity and other additives. \n\n2) Straight mineral oil. \n\n3) The same oil as the main lubricating oil system. \n\n4) Synthetic oil.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The HP discharge valves of a 2 stage air compressor suffer from build up of carbon deposits even though the correct maintenance is carried out on them. What is the most likely cause of this problem? \n\n1) Ineffective air intake filter. \n\n2) Worn scraper and piston rings. \n\n3) Compressor cooling water temperature too low. \n\n4) Water in the compressor lubricating oil.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Which of the following terms is used to describe a thermodynamic process in which no heat transfer into or out of the system occurs? \n\n1) Isochoric. \n\n2) Isothermal. \n\n3) Adiabatic. \n\n4) Polytropic.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "The water cooling space on a turbocharger is damaged and there is no spare casing. The cooling water must be shut off. Which option would you take to keep the risk of further damage to a minimum? \n\n1) Run the engine at a lower speed. \n\n2) Make no modifications, but tell the duty engineer to pay special attention for abnormalities. \n\n3) Cool the turbocharger by means of air. \n\n4) Dismantle the rotor and assemble the sealing plates.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "The picture shows the component parts of a fluorescent light (items 10 to 14) above a circuit diagram (items 1 to 9). Between which terminals of the circuit should the ballast (or choke) be connected? \n\n1) 1 and 9 \n\n2) 3 and 4 \n\n3) 1 and 2 \n\n4) 5 and 6",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "What is the purpose of the relief valves fitted to the doors and casing of 2 stroke diesel engine crankcases? \n\n1) To release any vapour formed by lubricating oil coming into contact with a hot spot and so avoid overpressure in the crankcase. \n\n2) To relieve excess pressure in the crankcase resulting from a crankcase explosion. \n\n3) To maintain a constant pressure in the crankcase. \n\n4) To relieve excess pressure in the crankcase resulting from piston rod gland leakage.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "In what language/languages must the fire control plans or booklets (or copies of these) be written? \n\n1) In a national language where company head office is located \n\n2) In the Flag State official language \n\n3) In the Flag State official language with copies in English or French \n\n4) In the English language",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "An Oil Record Book, Part 1, shall be provided to every ship of 400 tons gross tonnage and above to record machinery space operations. Out of below mentioned operations, it is compulsory to record: \n\n1) Purification of HFO. \n\n2) Discharge of water from Aft, Peak Tank. \n\n3) Transfer of oil from settling - to daytank. \n\n4) Bunkering of bulk lubricating oil.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "What is the minimum furnace temperature that must be reached during start up before waste material can be introduced into an incinerator? \n\n1) 850 C \n\n2) 1500 C \n\n3) 2000 C \n\n4) 2500 C",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Which of the following requirements regarding life-buoys correspond to present regulations? (SOLAS III/7.1) \n\n1) At least four life-buoys on each side of the ship shall be fitted with buoyant lifelines \n\n2) Not less than half the total number of lifebuoys shall be provided with self-ignighting lights \n\n3) At least one lifebuoy with self-activating smoke shall be placed within the vicinity of the stern \n\n4) All the life-buoys shall be placed in holders with quick-release arrangement",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Spray painting has been carried out in the engine room while the engine was running, and the turbocharger intake filter was not protected. Which one of the options given is most likely to result from this? \n\n1) Scavenging air pressure is higher than normal \n\n2) Exhaust gas temperatures lower than normal. \n\n3) Scavenge air pressure lower than normal. \n\n4) The revolution of the turbocharger lower than normal.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "When considering instrumentation systems, what is the meaning of the expression 'dead-band'? \n\n1) It will take some time before the controller will react to a change \n\n2) The controller will enter 'sleep mode' \n\n3) The controller will is not respond to adjustment of set-point \n\n4) The controller will not react to a process change in this range",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Flow irregularities in pipes are not caused by: \n\n1) Straight pipe \n\n2) Restrictive valve \n\n3) Elbow pipe \n\n4) Throttling Valve",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "In a PID controller it is possible to change the setting of the Proportional band (P), the Reset time (I) and the Rate time (D). Please indicate which curve shows the typical response to a step change in input, if the setting of the reset time is too small. \n\n1) Figure 1. \n\n2) Figure 2. \n\n3) Figure 3. \n\n4) Figure 4.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "It is the Master's responsibility to ensure that: \n\n1) All information regaridng the onboard training is given to the ship manager \n\n2) concerned personnel carry out the on-board trainig programme effectively \n\n3) All personnel participate in the training at the same time \n\n4) safety equipment is not used during the training",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "During operation of a large slow speed diesel engine it is sometimes necessary to changeover from heavy fuel oil to diesel oil, for example before manoeuvring. How should this procedure be carried out? \n\n1) As quickly as possible to reduce steam heating requirement. \n\n2) As quickly as possible to reduce HFO consumption. \n\n3) Gradually to prevent gassing up of the fuel system due to overheating the diesel oil as it mixes with the hot heavy fuel oil.  \n\n4) As slowly as possible to reduce diesel oil consumption.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "For which ships is the SOLAS convention applicable? \n\n1) For passenger vessels only.\n\n2) For tankers and other vessels carrying persistent oil as cargo. \n\n3) For all vessels except passenger vessels. \n\n4) For all vessels. ",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "What percentage of the ship's stores are required to be inspected at Security Level 3? \n\n1) 100% of the ship's stores are required to be inspected at Security Level 3. \n\n2) 50-80% of the ship's stores are required to be inspected at Security Level 3. \n\n3) 5-20% of the ship's stores are required to be inspected at Security Level 3. \n\n4) 25-50% of the ship's stores are required to be inspected at Security Level 3.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Part of the outer surface of a refrigeration compressor crankcase and the refrigerant return line near the compressor ice up heavily during normal operation. Which of the options given is the most likely cause of this problem? \n\n1) The superheat control setting for the thermostatic expansion valve is set too low. \n\n2) The filter drier unit in the liquid line is partly blocked. \n\n3) The oil separator is not functioning correctly and is allowing lubricating oil to pass into the system. \n\n4) The seawater flow control valve for the condenser is faulty allowing insufficient cooling water flow.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "A rocket parachute flare reaches an altitude of \n\n1) not less than 450m \n\n2) not less than 300m \n\n3) not less than 40m \n\n4) not less than 180m",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "The exhaust temperature on one cylinder of a diesel engine is high; what is the most likely cause of this? \n\n1) Leaking inlet valves. \n\n2) Insufficient cylinder lubricating oil feed to the cylinder. \n\n3) Leaking exhaust valves. \n\n4) Reduced fuel delivery from fuel injection pump.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "During inspection and overhaul of a 2-stage reciprocating air compressor the main and bottom end bearing shells are found to be heavily scored with parts of the overlay and bearing metal breaking away. The crankshaft pins are found to have only very light surface scratches. Which of the given options is the best action to be taken to remedy the problem? \n\n1) Replace the bearing shells with new spares after cleaning out the crankcase and refilling with clean oil. \n\n2) Refit the shells and refill the crankcase with clean oil and run the machine so that the bearings wear themselves back in. \n\n3) Replace the bearing shells and crankshaft with new spares and refill the crankcase with clean oil. \n\n4) Clean up the bearing surface and crankshaft pins with scrapers and grinding paste and refit them. Refill the crankcase with clean oil.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The fuel consumption for the main engine is calculated using the readings from the supply and return flow meters which are of the positive displacement type. When compared to the quantities calculated from tank soundings and calibration tables and indicated on the contents gauges the consumption appears consistently high. Which of the options given is the most likely cause of this discrepancy? \n\n1) The return flow meter is giving a low reading due to internal wear. \n\n2) The tank calibration tables are incorrect. \n\n3) The tank contents gauges are calibrated for the wrong fuel type. \n\n4) The supply flow meter is giving too high a reading due to internal wear.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Master of every ship must provide: \n\n1) A link between the shipboard training officer and the company training officer ashore \n\n2) the training during crews working hours only \n\n3) Proper rest to the crew after each training programme \n\n4) Facilities to conduct training whenever required by the training officer",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "What is the top priority if an incident occurs in US waters (OPA-90) \n\n1) Any immediate action to prevent loss of time \n\n2) Protection of the environment \n\n3) Prevention of oil pollution \n\n4) Safety of ship and crew",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "What is the main precaution to be taken prior to engaging the turning gear for a diesel engine? \n\n1) Isolate the starting air supply. \n\n2) Open the indicator cocks. \n\n3) Open the crankcase doors. \n\n4) Transfer main engine control from control room to emergency control console.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The critical part of any bunkering operation may be considered to be when topping off the tanks at which stage the risk of overflow and spillage of fuel oil is greatest. What is the correct safe procedure to adopt to minimise this risk? \n\n1) Top off all of the tanks together to reduce the inflow rate into each tank. \n\n2) Reduce the bunker delivery flow rate and top off the tanks one at a time. \n\n3) Watch for oil coming up the sounding pipe and shut the tank valve just before it overflows. \n\n4) Shut off each tank as it overflows into the fuel oil overflow tank.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Occasionally the tie rods on a large slow speed diesel engine may fail in service. The mode of failure is usually a complete fracture of the tie rod due to excessive fatigue stress. Select, from the options given, the features of the surface of the fracture that would confirm a fatigue failure. \n\n1) The surface at the fracture would be crystalline in appearance with a full 'cup and cone' shape. \n\n2) The surface of the fracture would be serrated in appearance and at right angles to the axis of the tie rod. \n\n3) Part of the fracture surface would be uneven but smooth (burnished) with the remainder crystalline with part 'cup and cone' shape. \n\n4) The surface of the fracture would be crystalline in appearance and at an angle of approximately 45 degree to the axis of the tie rod.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Which one of the listed requirements regarding service and maintenance of life-saving appliances corresponds to present regulations? \n\n1) At least one member of the crew shall hold a repairman certificate for life-saving equipment\n\n2) Maintenance and repair of all life saving equipments shall be carried out by the certified ship staff only \n\n3) Maintenance and repair of all the life-saving equipments will be carried out ashore in work shop only \n\n4) Instructions for onboard maintenance of life-saving appliances in accordance with the regulations shall be provided ",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "The engine turns over normally when starting air is supplied but does not fire even though normal starting rpm is achieved. What could be the probable cause to this? \n\n1) Air in the fuel oil system. \n\n2) The turbocharger has not run up to normal full speed. \n\n3) The turning gear interlock has operated. \n\n4) The lubricating oil temperature is low.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "How will continuous low load operation influence the time between overhauls, tbo, for the cylinder covers and associated valves of a 4-stroke diesel engine? \n\n1) Increase the time between overhauls since the engine is not working as hard. \n\n2) Reduce the time between overhauls due to increased fouling. \n\n3) No influence at all, the required overhauls are unaffected by operating load. \n\n4) Increase the time between overhauls since fuel injectors work better at low load so combustion will be improved and the maintenance will be reduced.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Occasionally the tie rods on a large slow speed diesel engine may fail in service. The mode of failure is usually a complete fracture of the tie rod due to excessive fatigue stress. Select, from the options given, the features of the surface of the fracture that would confirm a fatigue failure. \n\n1) Part of the fracture surface would be uneven but smooth (burnished) with the remainder crystalline with part 'cup and cone' shape. \n\n2) The surface of the fracture would be serrated in appearance and at right angles to the axis of the tie rod. \n\n3) The surface at the fracture would be crystalline in appearance with a full 'cup and cone' shape. \n\n4) The surface of the fracture would be crystalline in appearance and at an angle of approximately 45 degree to the axis of the tie rod.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Which one of the listed requirements regarding service and maintenance of life-saving appliances correspond to present regulations? \n\n1) Maintenance and repair of all the life-saving equipments will be carried out ashore in work shop only \n\n2) Maintenance and repair of all life saving equipments shall be carried out by the certified ship staff only \n\n3) Instructions for onboard maintenance of life-saving appliances in accordance with the regulations shall be provided \n\n4) At least one member of the crew shall hold a repairman certificate for life-saving equipment",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "The engine turns over normally when starting air is supplied but does not fire even though normal starting rpm is achieved. What could be the probable cause to this? \n\n1) The lubricating oil temperature is low.  \n\n2) The turbocharger has not run up to normal full speed. \n\n3) The turning gear interlock has operated. \n\n4) Air in the fuel oil system.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "How will continuous low load operation influence the time between overhauls, tbo, for the cylinder covers and associated valves of a 4-stroke diesel engine? \n\n1) Reduce the time between overhauls due to increased fouling. \n\n2) Increase the time between overhauls since the engine is not working as hard. \n\n3) No influence at all, the required overhauls are unaffected by operating load. \n\n4) Increase the time between overhauls since fuel injectors work better at low load so combustion will be improved and the maintenance will be reduced.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "How will continuous low load operation influence the time between overhauls, tbo, for the cylinder covers and associated valves of a 4-stroke diesel engine? \n\n1) Increase the time between overhauls since the engine is not working as hard. \n\n2) Reduce the time between overhauls due to increased fouling. \n\n3) No influence at all, the required overhauls are unaffected by operating load. \n\n4) Increase the time between overhauls since fuel injectors work better at low load so combustion will be improved and the maintenance will be reduced.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "A temperature control system is exhibiting hysteresis. Checks on all of the system components show that they are functioning correctly. Which of the changes/modifications given in the options is most likely to correct this problem? \n\n1) Increase the pressure of the air supply to the controller. \n\n2) Fit a new temperature sensor with a narrower temperature range. \n\n3) Fit a valve positioner to the system. \n\n4) Slacken off the control valve gland.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "A 5V dc source has an internal impedance of 0.2 ohms. When a load of 2.3 ohms is applied what voltage will be measured at the source terminals? \n\n1) 4.8 V\n\n2) 5.0 V \n\n3) 5.2 V \n\n4) 4.6 V ",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "A water heating system with automatic temperature control uses steam as the heating medium and the temperature is controlled by a pneumatically operated valve. What would be an acceptable start up procedure of the system from cold state? \n\n1) Start the system up in manual mode and gradually increase the controller output signal until the temperature reaches the required value before changing over to automatic control. \n\n2) Start the system up in automatic mode with normal set point but with the steam supply to the control valve manually throttled in. \n\n3) Start the system up in automatic mode with normal set point so that the required temperature is achieved as quickly as possible. \n\n4) Start with the control valve in manual and use the hand jack to gradually increase the temperature by throttling the steam flow before changing to pneumatic control.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Once the Safety Management System is verified and working effectively, what document is issued to the ship? \n\n1) The I.S.M. Certificate \n\n2) The Safety Management Certificate \n\n3) The Document of Conformance \n\n4) The Document of Compliance",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "This circuit consists of a voltage source V, a change-over switch S, a resistor R and a capacitor C. The voltage/time figures 1 to 4 show changes in the voltage V(C) when the switch S is suddenly shifted from position 1 to 2 at time t = 0. Only one of the diagrams is correct. Which? \n\n1) Figure 1 \n\n2) Figure 4 \n\n3) Figure 3 \n\n4) Figure 2",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Which of the following requirements to ships stability for normal operation corresponds to present regulations? (NSCL 4/12.2) \n\n1) Centre of gravity shall be calculated with accuracy better than 5 percent. \n\n2) In waters with the danger of icing, loading of deck cargo must be approved by competent authority. \n\n3) The ship is loaded in such a manner that adequate stability is achieved in all loading condition. \n\n4) Unless otherwise stated in the approved stability calculation, the total weight of the deck cargo shall not exceed 50 metric tons.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "The pressure in the fresh water cooling system for a diesel engine is fluctuating while the engine is running. When the engine is stopped the pressure is steady. What is the likely cause of this problem? \n\n1) The fresh water expansion tank is empty. \n\n2) The fresh water circulating pump is damaged. \n\n3) The temperature in the fresh water cooling system is too low. \n\n4) The engine has a cracked cylinder liner or cylinder cover.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Which of the following is the minimum acceptable value of insulation resistance for High Voltage equipment? \n\n1) 100 M Ohms \n\n2) 100 k Ohms \n\n3) 1 M Ohms \n\n4) 1 G Ohms",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "During inspection and calibration of a cylinder unit, the liner is found to be worn in a cloverleaf pattern with maximum wear midway between the lubrication points. What action is necessary to rectify the problem? \n\n1) Increase the cylinder oil rate to neutralise the corrosive action of the combustion products or change to a more alkaline cylinder oil. \n\n2) Reduce the jacket cooling water temperature to avoid thermal stress of the cylinder liner. \n\n3) Contact engine maker for advice. \n\n4) Increase the jacket cooling water temperature to avoid surface condensation of any acidic products of combustion.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "U-tube manometers are often used to measure differential pressure. Which of the listed pressures are U-tube manometers mostly used for? \n\n1) Cargo pressure \n\n2) Low differential pressures \n\n3) High differential pressures \n\n4) Absolute zero pressure",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "One of the crossheads on a large, six cylinder, slow speed diesel engine has been severely damaged due to bearing failure. The connecting rod for the cylinder concerned is to be removed from the engine and the piston and damaged crosshead suspended in the engine so that it can be run on 5 cylinders. Which of the methods given in the options should be used to suspend the piston and crosshead? \n\n1) Raise the piston sufficiently high to allow the crosshead support pins/chains to be fitted and rest the crosshead on them (with piston attached and positioned above the scavenge ports). \n\n2) Raise the piston (with crosshead attached) to just above the scavenge ports and insert pieces of wood through the ports to rest the piston on. \n\n3) Remove the cylinder cover and lift the piston until the crown and skirt are clear of the liner and place two bits of angle iron across the liner top to rest the piston on. \n\n4) Remove the cylinder cover and connect the piston (with crosshead attached) to the engine room crane and position the piston so that it covers the scavenge ports.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The piston rod of a large two stroke diesel engine has been damaged and is heavily scored in the way of the piston rod gland (stuffing box). It has been decided that it is economically viable to recondition the rod at a shoreside facility. Select, from the options given, the most suitable repair method that should be used. \n\n1) Recondition the rod by surface grinding and build up using plasma spraying with metal similar to the original. \n\n2) Recondition the rod by surface grinding and build up using chrome plating to give a harder running surface and avoid similar damage in the future. \n\n3) Recondition the rod by build up using electric arc welding and surface grinding. \n\n4) Recondition the rod by machining away the score marks and fit undersize rings to the stuffing box.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "In large 2 stroke diesel engines with oil cooled pistons it is normal practice to maintain circulation of the cooling oil for a period after the engine has stopped. Why is this done? \n\n1)  To allow the piston cooling oil to cool down.. \n\n2) To allow the piston cooling oil pump and motor to cool down gradually... \n\n3) To remove residual heat from the pistons and avoid any coking of the trapped oil. \n\n4) To help keep the engine warm.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Some fuel oil and lubricating oil separators have a facility to control the back pressure of the clean oil outlet during start up and operation. What is the purpose of this control function? \n\n1) To assist in discharging the bowl contents during the sludge cycle.  \n\n2) To reduce the amount of sealing water required during operation. \n\n3) To control the amount of fuel passing through the separator. \n\n4) To help to maintain the oil/water interface at the correct position.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "This is a typical emitter follower. What is the main reason for use of an emitter follower? \n\n1) The input impedance is made much larger than the output impedance \n\n2) The V out is always equivalent to the V in \n\n3) The collector can be connected to as high voltage as 10 V DC \n\n4) The input impedance is made much smaller than the output impedance",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Which of these precautionary measures can reduce the threat of piracy, if implemented? \n\n1) Plan to arrive at port at night. \n\n2)  Sail at full speed. \n\n3) Stay at least 15nm away from the shore. \n\n4) Turn off all of the ship's lights at night.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "These circuits are all active filters. Which of the circuits is a low-pass filter? \n\n1) Figure D  \n\n2) Figure C \n\n3) Figure B \n\n4) Figure A",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "In the circuit diagram shown the starter connects between which terminals? \n\n1) 7 and 8 \n\n2) 1 and 2 \n\n3) 3 and 4 \n\n4) 5 and 6",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Under ISM, what is a 'non-conformity'? \n\n1) An observed situation where objective evidence indicates the non-fulfilment of a specified requirement \n\n2) The wearing of non-standard Personal protective equipment \n\n3) Official log book entries not being completed correctly \n\n4) A safety officer not being nominated for the vessel",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Which of the following is a cause of loss of electrolyte in a battery cell? \n\n1) Decompression of cell \n\n2) All of the above \n\n3) High temperature during charging \n\n4) Overvoltage, overcharge, or faulty charger",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "In what kind of measuring equipment might we find a Bourdon-tube? \n\n1) In a temperature transmitter. \n\n2) In an A/D converter. \n\n3) In a pressure transmitter. \n\n4) In a flow metre.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "The mandatory color of a hand flare is: \n\n1) White \n\n2) Green \n\n3) Yellow \n\n4) Red",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Once the Safety Management System is verified and working effectively, what document is issued to the ship? \n\n1) The Safety Management Certificate \n\n2) The I.S.M. Certificate \n\n3) The Document of Conformance \n\n4) The Document of Compliance",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "This circuit consists of a voltage source V, a change-over switch S, a resistor R and a capacitor C. The voltage/time figures 1 to 4 show changes in the voltage V(C) when the switch S is suddenly shifted from position 1 to 2 at time t = 0. Only one of the diagrams is correct. Which? \n\n1) Figure 4 \n\n2) Figure 1 \n\n3) Figure 3 \n\n4) Figure 2",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Which of the following requirements to ships stability for normal operation corresponds to present regulations? (NSCL 4/12.2) \n\n1) Centre of gravity shall be calculated with accuracy better than 5 percent. \n\n2) In waters with the danger of icing, loading of deck cargo must be approved by competent authority. \n\n3) The ship is loaded in such a manner that adequate stability is achieved in all loading condition. \n\n4) Unless otherwise stated in the approved stability calculation, the total weight of the deck cargo shall not exceed 50 metric tons.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "The pressure in the fresh water cooling system for a diesel engine is fluctuating while the engine is running. When the engine is stopped the pressure is steady. What is the likely cause of this problem? \n\n1) The fresh water expansion tank is empty. \n\n2) The fresh water circulating pump is damaged. \n\n3) The temperature in the fresh water cooling system is too low. \n\n4) The engine has a cracked cylinder liner or cylinder cover.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "It is noticed that some of the items that were to be used to lift some machinery components during a maintenance routine had not been tested for over 5 years. Which of the options given is the correct action to be taken in a situation like this? \n\n1) Have them inspected immediately by a competent person so that they can be used for the task. \n\n2) Scrap the items immediately as they are unusable once they have not been tested for 5 years. \n\n3) Return them to the lifting gear locker and make a note in the Register of Lifting Gear that they need to be tested. \n\n4) Mark the items as not to be used and store them securely until they can be tested by a competent person.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Shortly after starting up a fuel oil purifier oil is seen to be trickling out of the sludge outlet. Which of the options given is the most likely cause of this problem? \n\n1) Excessive back pressure in the clean oil outlet. \n\n2) Incorrect gravity disc fitted. \n\n3) Insufficient seal water supplied during start up. \n\n4) Damaged bowl seal.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Why is input aliasing important in digital process control? \n\n1) It reduces noise dampening in digital process control \n\n2) It increases accuracy and precision of process measurement \n\n3) It reduces lag and deadtime in digital process control \n\n4) If frequency of signal sampling is not fast enough, digital representation of original signal will not be accurate",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "What is the maximum current that a 15 Volt, 3 Watt Zenerdiode can handle without damage? \n\n1) 0.5 A \n\n2) 20 A \n\n3) 0.45 A \n\n4) 0.2 A",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "It is noticed that some of the items that were to be used to lift some machinery components during a maintenance routine had not been tested for over 5 years. Which of the options given is the correct action to be taken in a situation like this? \n\n1) Have them inspected immediately by a competent person so that they can be used for the task. \n\n2) Scrap the items immediately as they are unusable once they have not been tested for 5 years. \n\n3) Return them to the lifting gear locker and make a note in the Register of Lifting Gear that they need to be tested. \n\n4) Mark the items as not to be used and store them securely until they can be tested by a competent person.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Shortly after starting up a fuel oil purifier oil is seen to be trickling out of the sludge outlet. Which of the options given is the most likely cause of this problem? \n\n1) Excessive back pressure in the clean oil outlet. \n\n2) Incorrect gravity disc fitted. \n\n3) Insufficient seal water supplied during start up. \n\n4) Damaged bowl seal.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Why is input aliasing important in digital process control? \n\n1) It reduces noise dampening in digital process control  \n\n2) It increases accuracy and precision of process measurement \n\n3) It reduces lag and deadtime in digital process control \n\n4) If frequency of signal sampling is not fast enough, digital representation of original signal will not be accurate",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "What is the maximum current that a 15 Volt, 3 Watt Zenerdiode can handle without damage? \n\n1) 0.5 A \n\n2) 20 A \n\n3) 0.45 A \n\n4) 0.2 A",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Which one of the options given is the most likely cause of a diesel engine failing to turn on air when the start signal is initiated? \n\n1) Slight leakage at the indicator cocks. \n\n2) Start air compressor has cut out due to sufficient pressure in system. \n\n3) Auxiliary blower is operating. \n\n4) An interlock or blocking device in the remote starting system is operating.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Who is responsible for maintaining the vessel's structural strength? \n\n1) The management company. \n\n2) The flag state administration. \n\n3) The classification society. \n\n4) The master.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "When work must be done on High Voltage equipment, it is vital that the equipment is earthed (grounded) after isolation procedures have been carried out. Why is this so? \n\n1) To provide a reference point, and so ensure accuracy of any test results. \n\n2) To ensure that the equipment does not overheat due to currents circulating through earth (ground). \n\n3) To ensure that it is dead, even if there was a flaw in the isolation procedure. \n\n4) To ensure that no energy remains in the system and that it cannot be recharged by external influences.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "What is definition on clean ballast as per MARPOL Annex I? \n\n1) Ballast with an oil content of less than 15 ppm \n\n2) Ballast with an oil content of less than 1% \n\n3) There isn't any definition on clean ballast \n\n4) Ballast with an oil content of less than 45 ppm",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "What is the function of a compounding Control Automatic Voltage Regulator (AVR) in generator excitation? \n\n1) To maintain prime driver speed of generator \n\n2) To increase current to correct value \n\n3) To increase electromagnetic field to acceptable range \n\n4) To trim down current to correct value",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "What is the normal slow down/shutdown temperature for the jacket cooling water outlet from a diesel engine cylinder? \n\n1) 105 - 108 °C\n\n2) 85 - 88 °C  \n\n3) 75 - 78 °C \n\n4) 95 - 98 °C",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "The International Maritime Bureau Piracy Reporting Centre attributes the increased numbers of hijackings to: \n\n1) More crew involvement. \n\n2) Higher crime rates around the world. \n\n3) Easy access to military weapons. \n\n4) The greater involvement in piracy of well-organized and armed crime networks.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "A vessel which normally operates with the engine room in UMS mode is unable to do so because of defects to some of the critical alarm functions. What are the main considerations that the Chief Engineer must take into account when planning alternative arrangements to cover the engine room requirements until the defects are cleared? \n\n1) A work rota is established to ensure that normal routine maintenance is carried out on time in accordance with the planned maintenance schedule. \n\n2) A work rota is established to ensure at least one person is in the engine room at all times while the defects exist. \n\n3) A work rota is established to ensure that the necessary repairs can be carried out as soon as possible. \n\n4) A work rota is established to ensure full coverage of engine room watchkeeping duties and adequate rest periods for the engineering staff.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "What kind of electrolyte is used for Nickel-iron batteries? \n\n1) Solution of sulphuric acid and water \n\n2) Solution of sodium and water \n\n3) Solution of zinc-carbon and water \n\n4) Solution of potassium hydroxide (KOH) and water",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "A large 2 stroke engine is normally controlled from the bridge during manoeuvring. In this type of automated control for the starting system what would normally cause the 'Engine Failed to Start' alarm to be activated and to lockout starting from the bridge? \n\n1) 3 failed start attempts if the start air pressure had fallen to less than a set value. \n\n2) 3 failed start attempts. \n\n3) Low start air pressure irrespective of the number of failed start attempts. \n\n4) A single failed start attempt.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "A refrigeration plant is short cycling even though there is plenty of refrigerant in the system and all of the rooms are above temperature. From the options given select the one which is the most likely cause of the problem? \n\n1) Ice formation in the meat room evaporator coil causing the automatic low pressure cut out to operate. \n\n2) Low oil level in the sump causing the automatic low oil pressure cut out to operate. \n\n3) Blocked filter drier causing the automatic low pressure cut out to operate. \n\n4) Insufficient cooling water flow through the condenser causing the automatic high pressure cut out to operate.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "One cylinder of a diesel engine has to be cut out to allow continued operation of the engine. Which of the following options may be the cause of the problem? \n\n1) Low charge air pressure. \n\n2) Gas side of turbocharger fouled. \n\n3) Camshaft timing incorrect. \n\n4) Injection pump failure.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "To maintain a good relationship among the crew on board a vessel, one must be: \n\n1) Understanding, Co-operative, and have respect from both sides \n\n2) Give authority to others \n\n3) Polite and diplomatic while talking to crew members \n\n4) Strict and authoritative while giving orders",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "When a pollution incident occurs there is a plan for actions to be undertaken. State which of following priority sequences to be considered: \n\n1) Stop pumps - clean up - report? \n\n2) Stop pumps - report - clean up \n\n3) Report - stop pumps - clean up \n\n4) Clean up - report - stop pumps?",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Which is the preferred method for starting an air conditioning refrigeration compressor which has been shut down for a period of time? \n\n1) Start with the discharge valve throttled in to prevent excess condenser pressure. \n\n2) Start with all system valves fully opened. \n\n3) Start with suction valve throttled in to minimize risk of drawing liquid refrigerant into the compressor. \n\n4) Start and stop repeatedly until suction pressure and oil pressure are normal.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Over a period of a few hours of operation the main diesel engine speed gradually falls off. From the options given what is the most likely cause of this fault? \n\n1) Water in a cylinder. \n\n2) Injection valve opening pressure is too low. \n\n3) Governor linkage broken. \n\n4) Fouling of turbocharger intake filters.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "A combustible gas indicator of the catalytic filament type is used to check the atmosphere in an enclosed space onboard ship. When taking readings in a fuel tank which has been emptied for cleaning the meter reading initially rises and then falls back to zero. What is the likely defect, if any, in the instrument when this type of behaviour is displayed? \n\n1) The filament is contaminated due to too high a concentration of hydrocarbons. \n\n2) The filament has burnt out. \n\n3) The batteries are flat. \n\n4) The sampling pump is faulty.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "When should a crew member joining a ship for the first time be given some training and instructions in the use of the ship's fire-fighting appliances? \n\n1) As soon as possible but not later than 2 days after he joins the ship \n\n2) As soon as possible but not later than 2 weeks after he joins the ship \n\n3) As soon as possible but not later than 24 hours after he joins the ship \n\n4) As soon as possible",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "The temperature of the feed water for an auxiliary boiler is automatically controlled by a pneumatically actuated steam valve at the inlet to the pre-heater. It is noticed that during high demand the temperature falls by an unacceptable amount and takes a long time to return to the set temperature even though the steam supply pressure remains constant. Select from the options given the most likely cause of this. \n\n1) The controller reset time is set too long. \n\n2) The control air pressure regulator is set too low. \n\n3) The controller proportional band is set too wide and the reset time is set too long. \n\n4) The controller proportional band is set too wide.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "The image shows an indicator diagram taken from a diesel engine cylinder. Which of the following options is the action most likely to identify the fault? \n\n1) Check if the fuel pump injection is too early, or fuel pump lead is too great, for that cylinder. \n\n2) Check that the fuel temperature and viscosity are correct. \n\n3) Check if the fuel injection valve is partly blocked. \n\n4) Check the exhaust valve.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "What would be a typical value for the set point for shut down of a large 2-stroke diesel engine due to thrust bearing high temperature? \n\n1) 125°C \n\n2) 65°C \n\n3) 105°C \n\n4) 85°C",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Oil analysis results for a sample of diesel engine lubricating oil show a high level of tin. What could be the possible cause? \n\n1) Cylinder oil contamination of the lubricating oil system. \n\n2) Debris from damage to a white metal bearing. \n\n3) Debris from damage to a rolling contact bearing. \n\n4) Debris from fretting between bearing housing parts",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "You have to choose one of the following instruments for measuring pressure in an air bottle in measuring range 0 - 35 BAR. Which instrument would you install? \n\n1) U-type Hg manometer \n\n2) U-type H2O manometer \n\n3) Bourdon Tube manometer  \n\n4) Bellow type manometer",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "The instrument air system is suffering from excess water carry over to the instrument air lines. The air intake to the compressor has very high humidity. Which of the actions given in the options will most likely result in reducing this problem? \n\n1) Increase the cooling water flow through the compressor intercooler and aftercooler. \n\n2) Use an additional coalescer filter in the inlet to the instrument air filter system. \n\n3) Shorten the time between automatic receiver drain blow downs. \n\n4) Reduce the superheat setting on the instrument air refrigeration/dryer unit.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "On all UMS operated vessels and also on most other vessels the engine room is equipped with fire detectors. What requirements of testing and checking of the detectors are to be observed? \n\n1) All the mentioned alternatives. \n\n2) When testing detectors by suitable sensors self controlling system, e.g., a flashing control light etc., is functioning. \n\n3) Check that the actual detector is giving appropriate signals to the central control unit and that all electric connections are in good order. \n\n4) Check the detector with heat and/or smoke (in accordance with instructions in its manual)",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Which of the 4 alternatives shows a NPN bipolar transistor? \n\n1) Figure 4. \n\n2)Figure 3.  \n\n3) Figure 2. \n\n4) Figure 1.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Which of the following symptoms would indicate that the filter drier in a refrigeration circuit has become blocked? \n\n1) A pressure rise before the drier. \n\n2) A hammering noise from the drier. \n\n3) A large temperature drop across the drier. \n\n4) A hammering noise from the compressors.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "The auxiliary boiler for the supply of low pressure heating steam has an automatic combustion control which operates on a two step control principle. The boiler fails to attempt to start up during a period of normal operation even though the steam pressure has fallen below the set point. What is the most likely cause of this fault? \n\n1) The electrical supply for the control system is isolated. \n\n2) The pressure switch for the combustion air supply is faulty and remains open. \n\n3) The photocell for detecting flame on is dirty. \n\n4) The pressure switch for low steam pressure is faulty and fails to close.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "During helicopter evacuation of an injured man, what course should the ship steer? \n\n1) As instructed by the helicopter pilot \n\n2) With the wind astern so that the effect of the wind is reduced as much as possible \n\n3) With the wind fine on the bow opposite to the helicopter operating area \n\n4) Directly into the wind",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Continuity testing of a delta connected three phase induction motor yields the following results; U1-V1 = 4 ohms, V1-W1 = 4 ohms, W1-U1 = 4 ohms. What is the value of continuity resistance for each winding ie. U1 - U2? \n\n1) 4 ohms \n\n2) 6 ohms \n\n3) 2 ohms \n\n4) 12 ohms",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "A 250V contactor has been fitted to a 220V supply. Which of the following symptoms might be observed? \n\n1) Contactor constantly on \n\n2) Contactor overheating \n\n3) Contactor chattering (vibrating) \n\n4) Contactor wont operate",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "An indicator card from a cylinder of a slow speed diesel engine shows a high maximum pressure occurring earlier in the cycle than normal with a normal compression pressure. From the options given, which action is most likely to identify the cause of the problem? \n\n1) Check if the fuel filters are blocked. \n\n2) Check if the fuel injection valve is partly blocked. \n\n3) Check if the fuel viscosity and temperature are correct. \n\n4) Check if the fuel injection pump timing is correct.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "In a closed loop control system the error signal is derived from which of the following? \n\n1) The demand and the feedback signal \n\n2) The process and the feedback sensor \n\n3) The tolerance of the feedback sensor \n\n4) The process and the demand",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Are there any exceptions from OPA-90? \n\n1) Yes, close to any US naval base \n\n2) Yes, transit passage through US waters to a non US port \n\n3) No exceptions \n\n4) Yes, if the vessel calls a US port for only a short stop",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "When the vessel is operating in a tropical area with very high humidity, what action should be taken to deal with the expected increase in condensate from the main diesel engine's charge air cooler? \n\n1) Decrease the scavenge air temperature to minimise the condensate from the charge air cooler. \n\n2) Increase the scavenge air temperature to minimise the condensate from the charge air cooler. \n\n3) Ensure that condensate drains from the water separator are monitored and operating correctly. \n\n4) Reduce the engine load to minimise condensate from the air cooler.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "To avoid overbunkering and oil spill, it is very important that we closely monitor the progress of the bunkering operation. What is the safest method to use to minimise the risk of overflow and spillage? \n\n1) Continuously monitor remote gauge readings and confirm with regular sounding of the fuel tanks. \n\n2) Use the predicted loading rate to calculate how much oil is being received. \n\n3) The remote gauge system will provide us with the necessary information \n\n4) Open all the bunker tank lids to manually watch them filling.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "What is the result of a \"high metacentric height\"?\n\n1) The vessel's tweendeck heights is too high \n\n2) The vessel will roll slowly or be unstable\n\n3) The vessel will have a great bending moment\n\n4) The vessel will roll violently",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "A heat exchanger of the tube and shell type is used for cooling lubricating oil with seawater as the secondary fluid. Which of the options would indicate that the tube stack was becoming fouled (scaled or coked) rather than blocked?\n\n1) A reduced temperature difference between the seawater inlet and outlet and also between the lubricating oil inlet and outlet.\n\n2) An increase in the temperature difference between the seawater inlet and outlet and the lubricating oil inlet and outlet.\n\n3) A reduced temperature difference between the seawater inlet and outlet and an increase in the temperature difference between the lubricating oil inlet and outlet.\n\n4) An increased temperature difference between the seawater inlet and outlet and also between the lubricating oil inlet and outlet.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "How often shall each member of the crew participate in an \"abandon ship\"-drill?\n\n1) Once every 6 months\n\n2) Once every month\n\n3) Once a year\n\n4) Once every week",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "In the context of an automated process control system, what is understood by the term Master Controller?\n\n1) The best possible control system\n\n2) The Captain's controller\n\n3) The primary controller in a cascade control system\n\n4) State of the art controller",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Buoyant smoke signals shall be so designed as to burn or emit smoke:\n\n1) Continuously after having been immersed for a period of 1 minute under 1m of water\n\n2) Only when not in the water\n\n3) When under water\n\n4) Continuously after having been immersed for a period of 10 seconds under 100 mm of water when underwater",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "When starting three phase induction motors which of the following starting methods will immediately apply rated voltage to the machine?\n\n1) Direct on Line\n\n2) Auto - transformer\n\n3) Star Delta\n\n4) Soft starter",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Which one of the listed requirements regarding life-saving appliances corresponds to present regulations?\n\n1) All prescribed life-saving appliances shall be of such a colour that they are in contrast to the surrounding colour \n\n2) All prescribed life-saving appliances shall be made of non-combustible or fire retardant material\n\n3) All prescribed life-saving appliances shall be fitted with the manufacturers name and Logo\n\n4) All prescribed life-saving appliances shall have marking in red colour",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "How does the maximum oil film pressure in a white metal journal bearing operating under full fluid film conditions compare with the pressure of the lubricating oil supply system?\n\n1) The pressure is the same as the pressure in the lubricating system regardless of the journal load. \n\n2) The pressure is greater than the pressure in the lubrication and is constant regardless of the journal load.\n\n3) The pressure is greater than the pressure in the lubricating system and varies with the journal load.\n\n4) The pressure is less than the pressure in the lubricating system and varies with the journal load.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "In the event of a diesel engine crankcase explosion which of the safety devices fitted to the engine is designed to minimise the risk of a secondary explosion?\n\n1) Main bearing temperature monitoring equipment.\n\n2) Crankcase extraction fan.\n\n3) Crankcase oil mist detector.\n\n4) Crankcase relief valves/doors",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "During maintenance work on the main engine a problem arises regarding the lifting of a main component in that the manufacturer's instructions do not apply to the engine as fitted and present a hazard. In which of the information/ record sources given in the options, is it most important to record the information relating to this anomaly?\n\n1) ISM procedures in the ship's safety manual.\n\n2) Engine room log book.\n\n3) Engine room planned maintenance schedule.\n\n4) Safety officer's report.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "A draw card obtained from a cylinder of a large 2 stroke diesel engine shows that both cylinder compression and maximum pressures are low. Cards from other cylinders indicate normal operation. What is the likely cause of this problem?\n\n1) Faulty high pressure fuel pump.\n\n2) Faulty cylinder component (piston rings, liner, etc.)\n\n3) Faulty turbocharger.\n\n4) Excessive cooling of the charge air.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "What should be the healthy continuity resistance of a 220V, 2.2kW,10A heating element, when checked near to its rated operating temperature?\n\n1) 10 Ohms\n\n2) 0.1 Ohms\n\n3) 22 Ohms\n\n4) 220 Ohms",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "How frequently should reports from protection and environmental work be sent to shore based management?\n\n1) Every three years. \n\n2) Not mandatory to send reports.\n\n3) Biannually.\n\n4) Annually.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Which one of the given requirements regarding survival craft muster and embarkation arrangements corresponds to the present SOLAS regulations?\n\n1) Muster and embarkation stations shall be readily accessible from accommodation and work areas.\n\n2) Davit-launched survival craft muster and embarkation stations shall be arranged to enable stretchers to be placed in survival craft.\n\n3) Muster and embarkation stations are to be arranged separately to improve working conditions.\n\n4) Searchlights to be provided at the launching station.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "What is the main theme of modern safety practice?\n\n1) Health & Safety at Work Act \n\n2) Making use of Risk Assessment as a means to improving safety\n\n3) Use the same practice that has been in place for some time\n\n4) Consult the chief officer before commencing work",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Which of the following measures is to be taken when working with batteries?\n\n1) Add new acid electrolyte to batteries that are in use\n\n2) Keep the batteries in discharged state\n\n3) Recharge batteries immediately after discharge\n\n4) Install alkaline and lead-acid batteries in the same compartment",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)


        await add_question(test_id,
                           "A transformer, rated at 22 kVA, 440/220 Volts, 60 Hz, is used to step down the voltage for a lighting system. The low tension voltage is to be kept constant at 220 Volts. What load impedance connected to the low-tension side will cause the transformer to be fully loaded?\n\n1) 220 Ohms \n\n2) 22 Ohms\n\n3) 0.22 Ohms\n\n4) 2.2 Ohms",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "In a large, 2 stroke, main diesel engine cylinder lubricating oil is supplied directly through lubrication points cut into the cylinder liner. At what point during the cycle should the supply normally occur.\n\n1) As the piston rings pass the lubrication points.\n\n2) At Bottom Dead Centre.\n\n3) At Top Dead Centre.\n\n4) At mid-stroke of the piston.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "When there is a need to interrupt current flow in a high voltage system it may be very difficult to quench the electrical arc which is generated at the circuit breaker contacts. Which of the following arcing media is commonly found in high voltage marine switchgear?\n\n1) Air\n\n2) Vacuum\n\n3) Oil\n\n4) Water",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Telephones are being used to communicate between personnel onboard and ashore during a bunkering operation. What instruction would you give to ship personnel regarding action to take in the event of failure of the telephone communication during the operation?\n\n1) Use a crewmember as a messenger between personnel involved in the operation.\n\n2) Slow down the bunkering rate until alternative reliable communications are established.\n\n3) Stop the bunkering until alternative reliable communications are established\n\n4) Call the electrician, and get him to repair the telephone while the bunkering operation continues.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)


        await add_question(test_id,
                           "In a large, 2 stroke, main diesel engine cylinder lubricating oil is supplied directly through lubrication points cut into the cylinder liner. At what point during the cycle should the supply normally occur.\n\n1) At mid-stroke of the piston. \n\n2) At Bottom Dead Centre.\n\n3) At Top Dead Centre.\n\n4) As the piston rings pass the lubrication points.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "When there is a need to interrupt current flow in a high voltage system it may be very difficult to quench the electrical arc which is generated at the circuit breaker contacts. Which of the following arcing media is commonly found in high voltage marine switchgear?\n\n1) Vacuum\n\n2) Air\n\n3) Oil\n\n4) Water",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Telephones are being used to communicate between personnel onboard and ashore during a bunkering operation. What instruction would you give to ship personnel regarding action to take in the event of failure of the telephone communication during the operation?\n\n1) Slow down the bunkering rate until alternative reliable communications are established. \n\n2)Stop the bunkering until alternative reliable communications are established\n\n3) Use a crewmember as a messenger between personnel involved in the operation.\n\n4) Call the electrician, and get him to repair the telephone while the bunkering operation continues.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "When considering instrumentation systems, what is the meaning of the term \"Span\" of a transducer.\n\n1) The maximum output signal when you have a minimum process value\n\n2) The length between the mounting flanges\n\n3) The difference between maximum and minimum measurement that gives a standard output signal\n\n4) Type of standard output signal according to ISO and EN standards",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)


        await add_question(test_id,
                           "When considering instrumentation systems, what is the meaning of the term \"Span\" of a transducer.\n\n1) Type of standard output signal according to ISO and EN standards\n\n2) The length between the mounting flanges\n\n3) The maximum output signal when you have a minimum process value\n\n4) The difference between maximum and minimum measurement that gives a standard output signal",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Continuity testing of a delta connected three phase induction motor yields the following results; U-V = 3 ohms, V-W = 3 ohms, W-U = 6 ohms. Which of the following is the likely condition?\n\n1) Open circuit winding between W and U\n\n2) Short circuit between V and Earth\n\n3) Short circuit winding between W and U\n\n4) Partial fault between W and U",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "When tuning a cascade control system, which of the following actions should be done first?\n\n1) Adjust the slave controller with the master controller in auto mode\n\n2) Adjust the slave controller with the master controller in manual mode\n\n3) Adjust the master controller with the slave controller disabled\n\n4) Adjust both controllers at the same time",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "The diagram shows a thyristor (SCR) with a Resistor and Capacitor (R and C). Which of the following applications is the RC network performing?\n\n1) Allow bypass route for ac signals.\n\n2) Provide voltage smoothing for SCR power supply.\n\n3) Divert fast voltage spikes which may lead to uncontrolled switch on.\n\n4) Assist SCR switch on.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)


        await add_question(test_id,
                           "What is a Continuous Synopsis Record? \n\n1) A record of all security incidents\n\n2) A plan including all security measures onboard \n\n3) A plan for continuous maintenance of security equipment \n\n4) A record of the vessels history ",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Which one of the listed requirements regarding the stowage of a survival craft corresponds to present SOLAS regulations? Each survival craft shall be stowed: \n\n1) In a secure and sheltered position and protected from damage by fire or explosion. \n\n2) In a state of readiness so that two crew-members can prepare for embarkation and launching in less than 15 minutes. \n\n3) Wherever space is available. \n\n4) On the starboard side of the ship.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Which international convention deals with fire-fighting equipment etc. \n\n1) CRISTAL\n\n2) SOLAS  \n\n3) Load Line convention \n\n4) MARPOL",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "A galley hot plate uses a Nichrome / Magnesium Oxide heating element and is to be tested before being put into service for the first time. An insulation resistance test yields a reading of 0.3 M Ohm. Which action should be taken? \n\n1) Put the element into service. \n\n2) Discard the element. \n\n3) Apply reduced voltage to the element for a few minutes. Then retest and if ok put into service. \n\n4) Wash the element in a degreasing agent. Then retest and if ok put it into service.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)


        await add_question(test_id,
                           "When starting up an aerobic type sewage unit for the first time, or after manual cleaning, how should the bacterial process be initiated? \n\n1) By adding an activating agent to the inflowing sewage. \n\n2) By bypassing the grey water inflow and operating only with black water. \n\n3) By filling the unit with sewage and bubbling air through it for 48 hours prior to starting the discharge pump. \n\n4) By shutting off the air flow.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "MARPOL - Annex V. Disposal of garbage outside 'Special Areas': After unpacking spares, you are left with a limited amount of packing materials. Is this prohibited, if not, what will be the nearest distance to land for disposal into the sea of these materials? \n\n1) 3 miles\n\n2) 25 miles \n\n3) 12 miles \n\n4) This is prohibited ",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "What is the correct operation of the slow-turning facility fitted to some large 2 stroke main propulsion diesel engines? \n\n1) Slow turning should be carried out immediately the duty engineer gets notice of standby from the bridge. \n\n2) Slow turning should be set to operate automatically prior to engine start when engine has been stopped for 20 to 30 minutes during manoeuvring \n\n3) Slow turning should be set to operate automatically every 10 to 15 minutes when the engine is on standby. \n\n4) Slow turning should be set to operate automatically at finish with engines to allow the engine to cool down evenly.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "During a scavenge port inspection of a diesel engine the piston rings on all units were seen to display the signs of the early stages of microseizure. What action should be taken to ensure that the progress of microseizure is stopped and the rings recover? \n\n1) Increase cylinder oil feed to all units. Check the fuel quality and operation of fuel oil purifiers and filter. \n\n2) Run the engine at reduced load. \n\n3) Replace all of the piston rings \n\n4) Decrease cylinder oil feed to all units",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "Give the meaning of the following symbol \n\n1) Rocket parachute flare \n\n2) Survival craft portable radio \n\n3) Survival craft distress pyrotechnic signals \n\n4) EPIRB",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Maintenance is to be carried out on a diesel engine. How long after stopping the engine should the cooling water and lubricating oil be kept circulating in order to avoid any undue thermal stress from residual heat? \n\n1) 10 minutes is sufficient. \n\n2) At least 8 hours \n\n3) At least 24 hours. \n\n4) At least one hour.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Fluid flow is measured using a pneumatic differential pressure transmitter and is indicated on a direct reading instrument. The indicator is reading zero even though fluid is flowing through the system. When the flow rate changes the indicator initially registers a reading but then gradually returns to zero. From the options given select the probable cause of this condition. \n\n1) Diaphragm in the differential pressure transmitter is perforated. \n\n2) The connection to the differential pressure transmitter low pressure bellows is blocked. \n\n3) The connection to the differential pressure transmitter high pressure bellows is blocked. \n\n4) The I/P converter is faulted.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "With reference to piping and instrumentation diagram (P&ID), what does below symbol symbolize? \n\n1) Capacitor \n\n2) Orifice \n\n3) Flow element \n\n4) Battery",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)


        await add_question(test_id,
                           "Low voltage ships tend to have insulated neutral systems. What is the reason for this? \n\n1) If the neutral is not insulated then it may short to other conductors. \n\n2) It is more effective than insulating the live conductor \n\n3) In the event of an earth fault vital equipment will not trip \n\n4) It is easier to detect faults",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Which of the following options is the most likely to result in the maximum cylinder pressure for all cylinders on a diesel engine to be lower than normal? \n\n1) A leaking exhaust valve. \n\n2) A worn fuel injector. \n\n3) Camshaft timing advanced. \n\n4) Poor quality fuel.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Most minor oilspills are caused by: \n\n1) Major casualties \n\n2) Human error \n\n3) Equipment failure \n\n4) Unforeseeable circumstances",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "During inspection of a cylinder of a large slow speed diesel engine it is noted that there are hard deposits around the upper part of the piston crown above the top ring groove and also some evidence of scuffing on the liner wall. From the options given select the one which is the most likely cause of this problem. \n\n1) Cylinder oil with TBN to great for fuel grade is being used. \n\n2) The fuel oil being used has too high a sulphur and ash content. \n\n3) Insufficient cylinder oil is being supplied. \n\n4) The piston cooling is inadequate causing overheating.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "Which cell voltage is required to trickle charge a lead acid battery? \n\n1) 2.0 V \n\n2) 1.2 V \n\n3) 2.15 V \n\n4) 2.5 V",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "One of the Main Engine cooling pumps is down for maintenance. The rest of the cooling pumps are operating near full capacity with minimum margins on the maximum temperature limit. What should be the correct action to take with regard to UMS operation? \n\n1) Operate the engine room on manual mode until the maintenance is completed and the cooling pump is operational and switched to stand-by mode. \n\n2) Arrange frequent checks of the condition during the night otherwise operate in normal UMS-mode \n\n3) Hope that the alarm function and automatic temperature regulation will function correctly and switch to UMS-mode as normal \n\n4) Arrange with a rating 'on watch' in the engine room for the UMS period.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Why should the coil of an ac solenoid valve not be energised when it has demounted from the valve body? \n\n1) The coil will fail due to vibration. \n\n2) The coil will lose its residual magnetism \n\n3) The coil will jump around. \n\n4) The coil will overheat.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Why is it necessary to have an effective ballast water management plan which includes provision for changing out ballast in open water rather than discharging ballast in coastal waters? \n\n1) To avoid the introduction of non-indigenous species of marine life from one area to another. \n\n2) To keep the ballast water fresh in the ballast tanks during long voyages. \n\n3) To allow ballast tank inspections to be carried out during ballast passage. \n\n4) To ensure that ballast tanks are always pressed up during a ballast voyage to avoid free surface effects.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "This circuit shown is a logic gate with two 'high' input signals, A and B, and one output signal Q. Which type of logic function does the gate provide? \n\n1) NOR gate \n\n2) OR gate  \n\n3) NAND gate \n\n4) AND gate",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "The cold room temperature is almost at the cut out point in a vapour-compression refrigeration system. What should the refrigerant state be just after the evaporator if the system is correctly set up? \n\n1) Cold liquid at high pressure. \n\n2) Sub-cooled liquid at low pressure. \n\n3) Slightly superheated low pressure gas. \n\n4) Wet vapour at high pressure.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "The torsion meter for the main propeller shaft is reading high. The torque is sensed using the angle of twist principle with two clamp rings attached to the shaft at a fixed distance, with stationary proximity switches for measuring the angle of twist and also shaft speed fixed to a rigid stool. What is the most likely cause of the high reading? \n\n1) Circumferential slip of the after clamp ring in the opposite direction to shaft rotation. \n\n2) Circumferential slip of the forward clamp ring in the opposite direction to shaft rotation. \n\n3) Axial slip of one of the clamp rings to bring them closer together. \n\n4) Axial slip of one of the clamp rings to move them further apart.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Some diesel engines have alarm and slow down protection in the event of a fire in the scavenge boxes. Choose the option which would be a typical set point for giving a slow down of the engine in the event of a scavenge box fire? \n\n1) 50° C \n\n2) 40° C \n\n3) 150° C \n\n4) 120° C",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "The temperature control for a hot water system is very erratic with the temperature gradually rising and then suddenly falling and vice versa even though system demand is fairly constant. Which of the options given is the most likely cause of this problem? \n\n1) Control valve gland is over tightened. \n\n2) Control air pressure supply is too low. \n\n3) Controller integral action reset time is too fast. \n\n4) Control valve actuator diaphragm is ruptured.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "What would be a typical set point for emergency shut down of a large slow speed diesel engine due to 'lubricating oil inlet to camshaft' low pressure? \n\n1) 0.4 bar \n\n2) 1.5 bar \n\n3) 5 bar \n\n4) 0.1 bar",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Who can contact the Designated Person with their safety concerns? \n\n1) Senior officers only \n\n2) The Master only \n\n3) All crewmembers \n\n4) The company's shore staff only",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "A low exhaust temperature in one cylinder of a diesel engine is noticed during routine checks. Which of the options given is the most likely cause of this? \n\n1) Injection valve opening pressure is too low. \n\n2) Problem with the fuel quality or supply to the engine. \n\n3) Charge air pressure is too high. \n\n4) Some of the nozzle holes of the fuel injection valve are blocked.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "What would be a typical set point for emergency shut down of a large slow speed diesel engine due to 'lubricating oil inlet to camshaft' low pressure?\n\n1) 1.5 bar\n\n2) 0.4 bar\n\n3) 5 bar\n\n4) 0.1 bar",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The temperature control for a hot water system is very erratic with the temperature gradually rising and then suddenly falling and vice versa even though system demand is fairly constant. Which of the options given is the most likely cause of this problem?\n\n1) Control air pressure supply is too low. \n\n2) Control valve gland is over tightened.\n\n3) Controller integral action reset time is too fast.\n\n4) Control valve actuator diaphragm is ruptured.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Who can contact the Designated Person with their safety concerns?\n\n1) Senior officers only\n\n2) The Master only\n\n3) All crewmembers\n\n4) The company's shore staff only",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "A low exhaust temperature in one cylinder of a diesel engine is noticed during routine checks. Which of the options given is the most likely cause of this?\n\n1) Injection valve opening pressure is too low.\n\n2) Problem with the fuel quality or supply to the engine.\n\n3) Charge air pressure is too high.\n\n4) Some of the nozzle holes of the fuel injection valve are blocked.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "A tachometer for a diesel engine is reading erratically. The tachometer is of the non-contact type using magnetic proximity switches to generate the signal. What is the most likely cause of this problem?\n\n1) The proximity switch is loose on its mounting.\n\n2) The shaft magnet has fallen off.\n\n3) The shaft magnet has become demagnetised.\n\n4) The proximity switch has dirt on the outside casing.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The analyses of the smoke produced by a fire may give an interpretation of that fire. Which are the factors we should take into account?\n\n1) There is no possible interpretation of a fire according to the smoke\n\n2) Opacity, amount and colour\n\n3) Colour only\n\n4) Amount and opacity only",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "When carrying out repair or maintenance tasks involving hot work a hot work permit must be issued. Select the correct option from those given which completes the following statement. 'The permit for hot work...\n\n1) ...should only cover specific hot work tasks and be valid for a specified time period.'\n\n2) ...should only cover specific hot work tasks, be valid for a specified time period and be issued by the person carrying out the work.'\n\n3) ...is valid for completion of the specific hot work tasks irrespective of the time taken.'\n\n4) ...can cover any additional hot work that arises during the completion of the task during the specified time period.'",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The operating mode of a pyrotechnic signal depends essentially on:\n\n1) The weather conditions of the moment\n\n2) The fact that the user is on board a liferaft, a lifeboat or ship\n\n3) Instructions or diagrams printed on its casing by the manufacturer\n\n4) A definite standard process",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "How often must the Emergency Steering Gear be tested, and how is this information recorded in the OLB?\n\n1) Fortnightly, with signature of Chief Engineer and witness\n\n2) Monthly with signature of person carrying out test\n\n3) Monthly, with signature of Chief Engineer and witness.\n\n4) Every three months. Details of test with signatures of Master and witness",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "With respect to the ISM, what training in addition to lifeboat and fire drills must be carried out?\n\n1) Familiarization, and other drills identified as necessary by the ship\n\n2) The boat drill and fire drill should be adequate to meet your needs\n\n3) Bridge Team Management\n\n4) Mooring operations",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "What do you understand by the term Maximum Continuous Rating, MCR, of a diesel engine?\n\n1) The maximum speed that the engine can operate at continuously.\n\n2) The maximum load that the engine can operate at continuously.\n\n3) The maximum charge air pressure that the engine can operate at continuously.\n\n4) The maximum cylinder pressure that the engine can operate at continuously.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "How many annexes do we find in MARPOL and what is the content of annex 1?\n\n1) We find 4 annexes in MARPOL and annex 1 regulations for the prevention of pollution by garbage\n\n2) We find 1 annex in MARPOL and annex 1 regulations for the prevention of pollution by chemicals.\n\n3) We find 6 annexes in MARPOL and annex 1 is the regulations for the prevention of pollution by oil\n\n4) We find 5 annexes in MARPOL and annex 1 is the regulations for the prevention of pollution by sewage",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)


        await add_question(test_id,
                           "How often should the lifeboat wire falls be turned and renewed?\n\n1) Turned every 2 years and renewed every 4 years\n\n2) Renewed every three years\n\n3) Turned every 30 months and needs only to be renewed if the wire is in poor condition\n\n4) Turned at intervals of not more than 30 months and renewed every 5 years",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "The pressure control of a vessel's domestic water system, which includes a hydrophore tank pressurised by air, is achieved by stop/start of the fresh water pumps using pressure switches. How should the system be prepared for first use to give correct operation of the pressure control?\n\n1) Fill the hydrophore tank to approximately 75% full with water and then pressurise with air up to the pump cut out point.\n\n2) Pressurise the hydrophore tank with air to pressure and then allow the pump to fill the tank until it cuts out.\n\n3) Fill the hydrophore tank up with freshwater allowing it to compress the air already in the tank and then adjust the pump cut out to match the pressure in the tank when it is almost full.\n\n4) Fill the hydrophore tank completely with water and then pressurise with air up to the pump cut out point.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The turbocharger on a diesel engine is surging. Which one of the following options would be the most likely cause?\n\n1) Worn out bearings on the turbocharger\n\n2) Dirty scavenging air cooler on the air side\n\n3) Dirty rotor blades and nozzle ring.\n\n4) The lubrication oil pump is malfunctioning",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "After a couple of hours of operation the failure alarm sounds for a heavy fuel oil purifier which is operating on a timed automatic sludge cycle. Upon investigation the purifier is found to be running slowly and when opened up the casing and sludge outlet is heavily fouled with sludge in contact with the bowl. From the options given what is the most likely cause of this problem?\n\n1) The purifier bowl has not closed properly.\n\n2) The dirty oil throughput is excessive.\n\n3) The heavy fuel is unstable leading to excessive high viscosity sludge formation.\n\n4) The clutch for the drive shaft is worn and slipping.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)


        await add_question(test_id,
                           "What is usually the effect on G when the ship is damaged with water ingress?\n\n1) It rises\n\n2) It is unchanged\n\n3) It first rises then lowers\n\n4) It lowers",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "This amplifier circuit is a common configuration used to amplify the difference in voltage between two input signals. In this case it is input 1 and 2. What is this amplifier called?\n\n1) Differential amplifier\n\n2) Push-pull amplifier\n\n3) Common emitter amplifier\n\n4) Darlington connection amplifier",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "In the type of fluorescent lamp system shown in the illustration, which of the following indicates the purpose of the starter?\n\n1) To charge the ballast to a high inductive current, and then divert this current through the lamp.\n\n2) To pass current through the lamp heaters, and then interrupt the inductive striking current.\n\n3) To create a high starting current.\n\n4) To switch on current through the lamp, and to disconnect the ballast once the lamp has started.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Small oil spills on deck can be kept from going overboard by doing what?\n\n1) Plugging the sounding pipes\n\n2) Driving wooden plugs into the vents\n\n3) Plugging the scuppers\n\n4) Closing the lids on the vents",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)


        await add_question(test_id,
                           "For which of the following ships, is the MARPOL convention applicable?\n\n1) For all vessels except passenger vessels.\n\n2) For all vessels except those engaged in coastal trade.\n\n3) For tankers and other vessels carrying persistent oil as cargo.\n\n4) For all listed vessels.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "A vessel is scheduled to enter a SECA during a forthcoming voyage. What additional considerations must a Chief Engineer take into account when planning for this voyage?\n\n1) The availability of low sulphur fuel and the change over time required to ensure the system is clear of normal fuel prior to entry into the SECA.\n\n2) That the incinerator is shut down for the duration of the time the vessel is in the SECA.\n\n3) That there is sufficient room in the bilge holding tank to ensure no discharges of machinery space bilges takes place while the vessel is in the SECA.\n\n4) That all garbage is fully disposed of prior to entry into the SECA and suitable arrangements are made for retention while in the SECA.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "On-board training in the use of davit-launched liferafts (including inflation and lowering whenever practicable) must take place\n\n1) every 2 months\n\n2) every 4 months\n\n3) every 3 months\n\n4) every month",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "What is full form of VRP (OPA-90)?\n\n1) Vessel Report Plan\n\n2) Vessel Response Procurement\n\n3) Vessel Response Plan\n\n4) Vessel Reporting Procedures",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)


        await add_question(test_id,
                           "Why is an automatic slow turning feature included in the start air system of many large 2 stroke diesel engines?\n\n1) To avoid damage during start of the engine in case water or other liquid has gathered in the cylinders during an extended stop.\n\n2) To reduce the start air consumption during start up of the engine.\n\n3) To check that all indicator cocks are closed before starting the engine.\n\n4) To fill the cylinders with sufficient fresh air to ensure a safe start of the engine.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "A motor nameplate reads 75 hp. What is the reading in kW?\n\n1) 128kW\n\n2) 37.5kW\n\n3) 75kW\n\n4) 56kW",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "In many cases the ship's Chief Engineer can carry out survey of machinery on behalf of a Classification Society under arrangements covering Continuous Surveys. As part of this arrangement a Surveyor from the Classification Society must carry out a periodic audit of the documentation for the approved planned maintenance system and undertake a confirmatory survey of the items surveyed. What is the normal frequency for this audit?\n\n1) Annual.\n\n2) Every 5 years\n\n3) Every 4 years.\n\n4) Bi-annual.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Sometimes an early warning of failure in High Voltage switchboards may produce an unpleasant smell. If the switchboard uses gas circuit breakers, which type of unpleasant smell may indicate a potential problem?\n\n1) Gas oil.\n\n2) Rotten eggs.\n\n3) Rotten fish.\n\n4) Chlorine.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)


        await add_question(test_id,
                           "What do you understand by the term \"Risk Assessment\", and how would this be carried out on board? \n\n1) States than when work has a degree of risk that the work is not carried out  \n\n2) Identify the hazards and specify the personal protective equipment that would be required to complete the work \n\n3) Identify the hazards, quantify the risks, put control measures in place, monitor the work activity and review\n\n4) Requires a great deal of preparation and involves recording everything on paper",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Which of the following is an application of a thermoelectric sensor? \n\n1) Proximity sensor \n\n2) Piezoelectric sensor \n\n3) Barometer \n\n4) Thermocouple",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "What should the expansion valve superheat setting be in order to get the best possible efficiency from a refrigerator evaporator? \n\n1) 5 - 10 degrees Celsius \n\n2) 40 - 50 degrees Celsius \n\n3) minus 18 Celsius \n\n4) 25 - 30 degrees Celsius",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "A Ship Security Assessment is integral to the creation of your ship's security plan. \n\n1) TRUE \n\n2) FALSE \n\n3) . \n\n4) .",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "Which of the following options would be a typical differential pressure setting for a main engine slow down in the event of jacket cooling water system low flow? \n\n1) 5 Bar \n\n2) 0.2 to 0.5 bar \n\n3) 10 Bar \n\n4) 1 to 2 bar.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "What are the main steps to convert an analogue signal to digital signal? \n\n1) Amplification, multiplexing, demodulation, A to D conversion \n\n2) Amplification, filtering, demultiplexing, A to D conversion \n\n3) Amplification, filtering, modulation, demodulation, A to D conversion \n\n4) Amplification, inversing, modulation, demodulation, A to D conversion",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "The figures show a graphical symbol for a particular electronic component and a typical working characteristic for the same component. Which component? \n\n1) Tunnel diode \n\n2) Zener diode \n\n3) Field effect transistor \n\n4) Silicon controlled rectifier (SCR)",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "What is the purpose of the O.D.M.E. (Oil Discharge Monitoring Equipment) printer? \n\n1) To prove that oil has been pumped overboard according to regulations \n\n2) To prove fault conditions in the O.D.M.E \n\n3) None of the mentioned \n\n4) To prove that the O.D.M.E. system has been used",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "What is the purpose of the air distributor in a diesel engine air start system? \n\n1) To ensure that the start air is distributed equally to the each of the engine cylinders. \n\n2) To ensure the cylinder air start valves operate in the correct sequence and for the correct period. \n\n3) To ensure the air consumption from each of the main air receivers is equally distributed. \n\n4) To ensure that the automatic valve in the air start system opens and closes at the correct time.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Which of the following tripping methods does not provide overcurrent protection? \n\n1) Electronic trip \n\n2) Electromagnetic trip \n\n3) Preferential trip  \n\n4) Thermal trip",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "When planning bunkering operations it is preferable to arrange for the new fuel to be bunkered into empty or nearly empty tanks whenever possible. What is the main reason for this? \n\n1) To minimise the risk of microbial contamination of the fuel. \n\n2) To make it easier to calculate the quantity of fuel taken onboard. \n\n3) So that the sulphur content of each fuel is known. \n\n4) To minimise the risk of incompatibility between different fuels.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Which two persons check the Declaration of Security? Select the correct pairing. \n\n1) The Port Facility Security Officer and the Ship Security Officer \n\n2) The Local Coast Guard Officer and the Port Facility Security Officer \n\n3) The Company Security Officer and the Ship Security Officer \n\n4) The Company Security Officer and the Port Facility Security Officer",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "The majority of conventions adopted under the auspices of IMO fall into which of the three main categories: \n\n1) There are no conventions that fall under IMO \n\n2) Maritime Safety, Prevention of Marine pollution, Liability and compensation \n\n3) Maritime Safety, STCW, Maritime Security \n\n4) Safety, Terrorism, ILO",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "In fresh water tank we are using a pressure transmitter with a range of 0-0.5 bar/4-20mA for level measurement. The transmitter is installed 30 centimetres from the bottom of the tank, and the tank is 5 meters high. What will the output from the transmitter be when the tank is empty? \n\n1) 2,8 mA \n\n2) 2 mA \n\n3) 4 mA \n\n4) 5,2 mA.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "A power card from a slow speed diesel engine cylinder is abnormal with a low height and the body of the diagram thicker than normal. What is the most likely cause of this? \n\n1) Fuel timing is advanced. \n\n2) Partially blocked fuel injection valve. \n\n3) Scavenge pressure is too high. \n\n4) Fuel timing is retarded.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "How can the pressure be regulated during start up of a positive displacement pump such as a gear pump? \n\n1) Adjustment of the pressure relief valve to recirculate part of the flow. \n\n2) By throttling the suction valve. \n\n3) Positive displacement pumps operate at constant pressure and cannot be regulated. \n\n4) By throttling the discharge valve",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "The fuel tank contents gauges onboard a vessel are of the air bubble and bell type. The gauges are calibrated for a different fuel type to the actual fuel in the tanks. When correcting the actual contents of the tanks from the gauge readings which of the parameters given in the options is the most important? \n\n1) Fuel pour point \n\n2) Fuel density \n\n3) Fuel viscosity \n\n4) Fuel temperature",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "During test and/or maintenance work of the CO2 system affecting the release system, precautions to ensure that the gas is not released into the engine room due to a mistake are to be ensured. What precautions should be taken? \n\n1) Arrange a watchman in the CO2 central.  \n\n2) No special precautions necessary. \n\n3) The main supply line to be blanked off prior to the work. \n\n4) Check the main valve for a potential leakage.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Why is it important that the correct tension is maintained in a diesel engine timing chain? \n\n1) Correct tension ensures that the fuel and valve timing are correct \n\n2) Correct tension ensures that there is absolutely no vibration in the chain. \n\n3) Correct tension ensures that the chain is correctly lubricated. \n\n4) Correct tension ensures that the chain and associated equipment is within normal loading limits.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "The pyrotechnics used to transmit visual signals to other vessels, boats or aircrafts are of the following type \n\n1) All of the below mentioned \n\n2) Hand flare \n\n3) Rocket parachute flare \n\n4) Buoyant smoke signal",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "Which ideal heat engine cycle is the vapour-compression refrigeration system based on? \n\n1) The Otto cycle. \n\n2) The reversed Carnot cycle. \n\n3) The Dual cycle \n\n4) The Rankine cycle.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "In a PID controller it is possible to change the setting of the Proportional band (P), the Reset time (I) and the Rate time (D). Please indicate which curve shows the typical response to a step input, if the variables are well adjusted. \n\n1) Figure 3. \n\n2) Figure 4. \n\n3) Figure 2. \n\n4) Figure 1.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "How should the spare oxygen and acetylene gas welding bottles be stored onboard the ship? \n\n1) In a refrigerated room. \n\n2) In the workshop in the engine room as close as possible to welding equipment. \n\n3) In the steering flat. \n\n4) In two separate rooms outside the engine room space.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "This graphical symbol is a logic gate. Which type of logic function does the gate provide? \n\n1) AND \n\n2) NOR \n\n3) OR \n\n4) NAND",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "When performing electrical testing of a three phase motor, insulation resistance measurements may be influenced by which of the following? \n\n1) Temperature, pressure and dampness \n\n2) Temperature, humidity and surface contamination \n\n3) Humidity, frequency and dampness \n\n4) Humidity, pressure and surface contamination",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "There are many applications in circuit theory where it is important to obtain the maximum possible power that a given source can deliver. What value of resistance R(L) will maximize the power transmission from the source to R(L)? \n\n1) R(L) = 0.5 R(S) \n\n2) R(L) = 2 R(S) \n\n3) R(L) = R(S) \n\n4) R(L) = R(S) / sqrt(3)",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Referring to the SOLAS convention, how often should a crew member on a cargo ship participate in one abandon ship drill and one fire drill? \n\n1) This is only required when he joins the ship \n\n2) Every second week \n\n3) Weekly \n\n4) Monthly",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Some ships generate electrical power at 440 Volts, but then step up this voltage to supply specific electrical equipment. One common example, may be to feed a large bow thruster. Why is this done? \n\n1) A large bow thruster will draw very large currents at low voltage. Being typically remote from the generator, significant voltage drops would occur at low voltage. \n\n2) The overall ship's electrical load does not justify High Voltage generating plant. This method allows more power to be delivered to the bow thruster at low running cost. \n\n3) The shipyard could not purchase High Voltage generating plant at the time of manufacture, so they used what was available at the time. \n\n4) Manufacturers can supply High Voltage bow thrusters at less cost, and the power factor is improved.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "Only search vehicle compartments where you suspect objects may be hidden. \n\n1) FALSE. \n\n2) . \n\n3) TRUE \n\n4) .",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "What is a Declaration of Security? \n\n1) A checklist jointly completed by the ship and shore security representatives \n\n2) A checklist jointly completed by the Ship Security Officer and the U.S. Coast Guard. \n\n3) A document between the port and the cargo owner stating security. \n\n4) A document stating the ship's security level.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The muster list shall show the duties assigned to the different members of the crew. Which of the given duties necessarily have to be included in the muster list? \n\n1) Preparation and launching of survival crafts \n\n2) Preparation and starting of emergency generator. \n\n3) Type of fires can be encountered on board. \n\n4) Clearing escape routes.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Some automated control systems use a master controller and a slave controller. What is the meaning of 'remote mode' in relations to a slave controller? \n\n1) The slave controller receives the set-point from the output signal of the master controller \n\n2) The slave controller can be in any mode of operation. \n\n3) The Slave controller can be tuned by a hand carried remote controller. \n\n4) The Slave controller can be tuned from the engine control room.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "A crosshead pin for a large bore 2-stroke diesel engine has to be refurbished following bearing failure. The surface finish required is measured as a centre line average, CLA. Select, from the options given, the standard of finish that should be achieved during the refurbishment. \n\n1) 5 to 10 micrometres CLA \n\n2) less than 1 micrometre CLA \n\n3) 10 to 20 micrometres CLA \n\n4) 1 to 5 micrometres CLA",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "A positive displacement type flow meter is defective and cannot be repaired. It is to be replaced with a new instrument which uses a Venturi type sensor. Which of the pneumatic relays given in the options will be required in order for this type of instrument to function correctly? \n\n1) Subtraction relay. \n\n2) Multiplier relay. \n\n3) Square root extractor relay. \n\n4) Summation relay.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "How is a Safety Management Certificate obtained? \n\n1) Vessel is surveyed by MCA and certificate issued \n\n2) RRS issue SMC with Register \n\n3) Ship owner is authorised to carry out internal audits and issue SMC \n\n4) Ship owner has Document of Compliance issued, and vessel is assessed and holds all statutory certificates ",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Which of the options given is likely to be the reason for a drop in the charge air manifold pressure of a diesel engine operating with an exhaust gas turbocharger? \n\n1) Exhaust gas boiler fouled. \n\n2) Scavenge ports dirty. \n\n3) Insufficient cooling of the charge air. \n\n4) Engine room exhaust fans stopped.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "From the options given, select the one which is most likely to result in a high exhaust temperature in one cylinder of a diesel engine. \n\n1) Speed governor defective. \n\n2) Scavenge ports of the one cylinder are dirty. \n\n3) Nozzle ring of turbocharger fouled or partially choked. \n\n4) Compression pressure too low.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "How can a lead-acid type battery be checked to confirm if it is fully charged or not? \n\n1) Measure the temperature of the electrolyte \n\n2) Measure the level of the electrolyte \n\n3) Measure the relative density (specific gravity) of the electrolyte \n\n4) Measure the battery voltage",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Which of the following is an application of a piezoelectric sensor? \n\n1) Proximity sensor \n\n2) Tachometer \n\n3) Thermocouple \n\n4) Accelerometer",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "The fuel injection timing of a diesel engine is delayed causing high cylinder exhaust gas temperatures. What is the likely effect of this condition on turbocharger operation? \n\n1) Increased turbocharger revolutions \n\n2) Decreased turbocharger revolutions \n\n3) Continuous surging of the turbocharger \n\n4) Vibration of the turbocharger.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "A plate type heat exchanger in a central cooling system has seawater leaking around the edges of some of the titanium plates. After inspection and reassembly following the manufacturer's instructions the problem still exists. What action, from the options given, should be taken to rectify the problem? \n\n1) Scrap the plates and replace with a new plate stack. \n\n2) Fit new gaskets to the each of the plates. \n\n3) Reduce the pressure of the sea water. \n\n4) Keep tightening the plate stack until the leakage stops.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "What is the function of a reference cell in a Impressed Current Cathodic Protection (ICCP) system? \n\n1) Facilitate monitoring of voltage of controller \n\n2) Discharges voltage to deter marine growth on the hull \n\n3) Measures the value of galvanic voltage with hull material \n\n4) Records daily measurement logs",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "The main propulsion diesel engine is normally started by direct admission of compressed air. Which one of the following statements is correct? \n\n1) A heavily leaking starting air valve may cause an explosion in the starting air pipe system. \n\n2) If the engine does not turn when the starting air is applied the turning gear can be used together with the starting air to start the engine. \n\n3) If the starting air pressure is too low a pressurized oxygen bottle from the welding equipment can be used for an emergency start of the engine. \n\n4) The starting air admission should continue until the engine has fired.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "What colour flare is used to signal a safe landing place for small boats? \n\n1) White \n\n2) Yellow \n\n3) Blue \n\n4) Green",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)


        await add_question(test_id,
                           "Some vessels have a central hydraulic system consisting of a number of hydraulic power packs for driving cargo pumps, deck machinery, ship's cranes, etc. Which parameter is normally used to automatically bring the power packs on and off line to match operational demand? \n\n1) Percentage of available flow. \n\n2) Percentage of maximum pressure being used. \n\n3) Temperature of hydraulic fluid. \n\n4) Number of consumers running (pumps, etc.).",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The steps of the embarkation ladder used must be proportioned as it follows: \n\n1) length = 280 mm, breadth = 85 mm, depth = 10 mm \n\n2) length = 480 mm, breadth = 115 mm, depth = 25 mm \n\n3) length = 380 mm, breadth = 145 mm, depth = 20 mm \n\n4) length = 580 mm, breadth = 165 mm, depth = 30 mm",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Consider a vessel with a 6 cylinder main diesel engine operating with one cylinder out of operation. What would you expect to be the approximate maximum reduced engine load to allow safe emergency operation in this condition? \n\n1) Approximately 90 % of MCR \n\n2) Approximately 30% of MCR. \n\n3) Approximately 70 % of MCR \n\n4) Approximately 50 % of MCR",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "What is the best way to avoid pollution from small oil-spills aboard a ship? \n\n1) Have sawdust ready for use \n\n2) Rig an oil boom around the ship \n\n3) Have dispersing chemicals ready for use in case of oil-spill \n\n4) Contain any oil-spill onboard the ship",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)


        await add_question(test_id,
                           "Worn piston rings are allowing a small amount of piston blow-by on a 2-stroke main diesel engine cylinder, but due to the circumstances, it is not possible to stop and do a piston overhaul. What is the correct, temporary action to take? \n\n1) Increase cylinder oil feed rate slightly and monitor the scavenge space drains. \n\n2) Reduce speed. \n\n3) Increase cylinder oil feed rate to the maximum. \n\n4) Continue to operate the engine as normal.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "In relation to OPA 90, Which of the following statements is correct? \n\n1) OPA-90 specify all oil cargo related rules and regulations \n\n2) COTP-zones may have additional rules and regulations \n\n3) After implementation of OPA-90 there are no area specific rules and regulations \n\n4) OPA-90 specify rules and regulations for all COTP-zones",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Is it necessary to be certified to be a lifeboat-commander? \n\n1) Yes, you must attend to a course held by certified personnel, and provide evidence of having maintained the required standards of competence every five years. \n\n2) No, the only thing you need is one hour instruction from a deck officer. \n\n3) No \n\n4) Yes, you must attend a one week course at a approved course center.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "You can reduce the need for security guards in certain areas by installing: \n\n1) Metal detectors \n\n2) Water cannons \n\n3) Anti-intruder devices \n\n4) Vapour detectors",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)


        await add_question(test_id,
                           "The circuit shows a full-wave bridge rectifier. Which electronic component should be connected between 'a' and 'b' in order to obtain reduced ripple voltage to the load RL. \n\n1) Zener diode \n\n2) Resistance \n\n3) Inductive reactor \n\n4) Capacitor",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Give the meaning of the following symbol \n\n1) Survival craft portable radio \n\n2) Rocket parachute flares \n\n3) EPIRB \n\n4) Survival craft distress pyrotechnic signals",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "When starting three phase induction motors there is sometimes a need to use a star-delta starter. Which of the following characteristics does a star-delta starter exhibits while connected in star? \n\n1) Reduced current and increased speed \n\n2) Reduced current and reduced torque \n\n3) Increased current and power \n\n4) Reduced current and increased voltage",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "The line voltage of a three phase system is 440V. What is the phase voltage? \n\n1) 147V \n\n2) 110V \n\n3) 254V \n\n4) 311V",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)


        await add_question(test_id,
                           "Which operating voltage level requires a mandatory work permit for maintenance purpose? \n\n1) Greater than 440V \n\n2) Greater than 690V \n\n3) Greater than 3.3kV \n\n4) Greater than 1kV",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Assign men to search men and women to search women unless a device such as a metal detector is used. \n\n1) TRUE \n\n2) . \n\n3) FALSE \n\n4) .",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Which of the following functions does the diode shown here perform? \n\n1) Allow Op Amp to top up +15V rail. \n\n2) Return inductive current to supply at switch off. \n\n3) Provide an overload route for transistor current. \n\n4) Reference the transistor to +15V.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "How long after starting a refrigeration compressor should the oil separator return valve be opened? \n\n1) It should be opened before start up. \n\n2) It should be opened only when the crankcase oil level is low. \n\n3) It should be opened once the oil separator unit has warmed up. \n\n4) It should be opened one minute after start up.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)


        await add_question(test_id,
                           "The operation of a diesel engine is controlled by a mechanical-hydraulic, compensated speed sensing governor. How will the governor control be affected if the compensation needle valve is closed in and the engine load changes? \n\n1) The governor will hunt resulting in erratic engine speed control. \n\n2) Altering the compensation needle valve has no effect on speed control. \n\n3) A change in load will not affect a speed sensing governor. \n\n4) Engine speed control will be sluggish.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Which of the following duties shall be included in the \"muster list\" as being assigned to crewmembers in relation to passengers? \n\n1) Assembling passengers at muster station \n\n2) Clearing the escape routes \n\n3) Ensuring that every passenger is provided with an immersion suit or a thermal protective aid \n\n4) Ensuring that extra food and water is taken to the survival craft",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "What are the main elements for Process Control? \n\n1) Resistor, Capacitor, Battery, Load \n\n2) Process, Sensor, Final control element and Controller \n\n3) Sensor, Controller, Noise, Final Control Element \n\n4) Sensor, Modulation, Controller, Process",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Prior to removing the access doors to a pressure vessel for internal maintenance it should be ensured that all pressure has been relieved. As well as a zero indication on a pressure gauge which other measure, from the options given should be taken to confirm this prior to commencing the work? \n\n1) Open the drain valve while pressure still shows on the gauge and to check it is clear. Outflow should cease as the pressure gauge reaches zero. \n\n2) Open the drain valve and when the outflow stops slacken off the drain valve flange bolts and 'crack' open the flange in case the drain is blocked. \n\n3) Open the drain valve when the gauge reads zero to check that there is no outflow. \n\n4) Back of the tensioning device for the relief valve to vent the pressure to atmosphere.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "Which of the following is not a fault rating of the circuit breaker? \n\n1) Asymmetrical breaking current \n\n2) Making current \n\n3) Short circuit current \n\n4) Symmetrical breaking current",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Can a ZENER BARRIER be installed in a hazardous area? \n\n1) Yes, that's what the zener barrier is made for. \n\n2) Only if properly marked for such installation. \n\n3) Only in equipment operating on very low voltage. \n\n4) No, as only the output from the barrier is intrinsically safe this is not allowed.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "The coil of a 12V, 120mA dc relay must be connected across a 24V supply. What action should be taken? \n\n1) Install a 100 ohm resistor in parallel with the coil \n\n2) Install a 100 ohm resistor in series with the coil \n\n3) Install a 100 k ohm resistor in parallel with the coil \n\n4) Install a 100 k ohm resistor in series with the coil",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "When trying to reverse a large slow speed diesel engine in the astern direction it cannot be turned on air even though it will start in the ahead direction. What is the likely cause of this problem? \n\n1) The reversing servo for the fuel pumps has stuck in the ahead position. \n\n2) The automatic valve for the air start system has jammed shut. \n\n3) The start is blocked because the air distributor has not moved to the astern position. \n\n4) One of the cylinder air start valves has stuck open.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)


        await add_question(test_id,
                           "High Voltage systems rely on the installed protective equipment being able to interrupt any fault in the system. Throughout the system, the fault level has been calculated, and under no circumstances must the system be modified to exceed this fault level. What is meant by fault level? \n\n1) The current level flowing into a symmetrical short circuit fault between all three phases. \n\n2) The amount of apparent power that could flow into any fault at any point in the electrical network. \n\n3) The amount of apparent power, that would be drawn from the generating plant, when a short circuit occurs at the bus bars. \n\n4) The current level flowing into a dead short to earth at any point on the ship, directly from the High Voltage system.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Temperature sensors may be marked T 802. What does this mean? \n\n1) 20 ohm at 802°C\n\n2) 100 ohm at 20°C \n\n3) 20 ohm at 100°C \n\n4) 802 ohm at 20°C ",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "When bunkering through the port side of the bunker manifold what action should be taken with the valves on the starboard side of the manifold prior to bunkering operations commencing? \n\n1) Blank flanges should be fitted to the closed starboard side manifold valves. \n\n2) Just check that the valves are closed. \n\n3) Just fit the blank flanges then it doesn't matter if the valves are closed or not. \n\n4) The blank flanges should be removed from the starboard side manifold valves to check for any leakage past the closed valves.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Why is it important to make weekly/routine rounds in the accommodation areas? \n\n1) To check for alcohol in cabins \n\n2) To ensure that cabins and common spaces are maintained in a clean, safe and hygienic condition \n\n3) It is a requirement as per flag state \n\n4) To search for any contraband goods hidden on board",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)


        await add_question(test_id,
                           "What must be done if the Oil Discharge Monitoring Equipment (ODME) should fail during a ballast voyage? \n\n1) The failure must be noted in the Oil Record Book \n\n2) The failure must be repaired \n\n3) All of the mentioned must be performed \n\n4) If the failure cannot be repaired onboard, the ODME must be repaired before the ship commences its next voyage",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "On board passenger ships an abandon ship drill must be performed: \n\n1) Every three months \n\n2) Every two weeks \n\n3) Every month \n\n4) Every week",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "On an oil tanker, are there any restrictions as to the maximum amount of treated water that originates from cargo spaces that has passed through a bilge water separator that can be discharged? \n\n1) Maximum is 30 litre pr nautical mile and total is 1/30000 part of full cargo on the ballast voyage. \n\n2) Maximum is 60 litre pr nautical mile and total is 1/30000 part of full cargo on the ballast voyage. \n\n3) Maximum is 30 litre pr nautical mile and total is 1/10000 part of full cargo on the ballast voyage. \n\n4) There isn't any restrictions of pumping sludge from ships outside special areas",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "What does the abbreviation SOLAS mean? \n\n1) International Conference for Security of Loads aboard Ships \n\n2) International Convention for the Safety of Lives at Sea \n\n3) International Rules for Safe Ocean Lines and Sailingroutes \n\n4) International Agreement for Security of Load and Ships",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)


        await add_question(test_id,
                           "*As far as human factor is concerned, which of the following actions should be considered as an efficient one? \n\n1) To establish inner rules to perform work of a special risk \n\n2) To equip them with better communication systems \n\n3) All the listed answers \n\n4) To train the fire brigade",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Every inflatable liferaft, inflatable lifejacket and hydrostatic release units shall be serviced: \n\n1) Every 24 months. \n\n2) Every 18 months. \n\n3) Every 36 months. \n\n4) Every 12 months.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "A U tube manometer is used to measure the pressure delivered by a ventilation fan. Following replacement of the fan by a larger unit with a higher delivery rate and pressure the liquid is blown out of the open end of the manometer. Which of the options given will allow the manometer to be used to measure the delivery pressure of the larger fan? \n\n1) Refill the manometer with liquid with a higher density. \n\n2) Refill the manometer with a reduced amount of liquid. \n\n3) Refill the manometer with liquid with a higher viscosity \n\n4) Connect the open end to the inlet trunking of the fan to measure the differential pressure rather than the delivery pressure.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The majority of marine diesel engines operate with either a pulse or a constant pressure turbocharging system. What is the main difference between these two systems? \n\n1) Pulse systems always have a turbocharger for each group of three cylinders. \n\n2) Constant pressure systems have all engine cylinder exhausts connected to a common large exhaust gas manifold. \n\n3) Constant pressure systems only ever have a single turbocharger irrespective of the number of cylinders on the engine. \n\n4) Pulse systems have all of the cylinder exhausts connected to a common large exhaust gas manifold.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)


        await add_question(test_id,
                           "A diesel engine is operating with retarded fuel timing resulting in increased exhaust gas temperatures. How would you expect this to affect the turbocharger? \n\n1) The turbocharger would operate normally. \n\n2) Decreased turbocharger revolutions. \n\n3) Increased turbocharger revolutions. \n\n4) Reduced air and gas temperature after turbocharger.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Some new maintenance routines are being planned and a risk assessment is necessary so that the required procedures can be entered into the ship's Safety Management manual. Which of the following should be the first step in this risk assessment process? \n\n1) Identify the hazards that may exist which may affect personnel involved with the maintenance routines. \n\n2) Identify who may be harmed or injured in carrying out the maintenance routines. \n\n3) Identify how much it will cost to implement the necessary precautions to prevent injury to personnel. \n\n4) Identify the safety precautions that may be necessary to prevent injury or harm to personnel carrying out the routines.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The wheatstone resistance bridge is often used for measuring resistances in, for example, Pt 100 temperature sensors or strain gauges. This figure shows such a bridge. Under what conditions will the bridge be balanced? i.e., the current through the meter i(m) = 0. \n\n1) R1 * R3 = R2 * R4\n\n2) R1 / R4 = R2 / R3 \n\n3) R1 + R3 = R2 + R4 \n\n4) R1 / R2 = R3 / R4 ",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "For a large 2-stroke diesel engine, what would be a typical set point for the low pressure shut down for the lubricating oil inlet to the main bearings? \n\n1) 10.0 bar \n\n2) 1.0 bar \n\n3) 5.0 bar \n\n4) 0.1 bar",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)


        await add_question(test_id,
                           "A thermistor which provides feedback for a thermal control system is suspected to have failed. Assuming there is no available direct/identical replacement for thermistor, which of the following methods may be used to prove it has failed? \n\n1) Connect a mV source in parallel with the thermistor connections. \n\n2) Disconnect the thermistor lead from the controller and replace with a mA source. \n\n3) Disconnect the thermistor lead from the controller and replace with a mV source. \n\n4) Connect a mA source in parallel with the thermistor connections.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "The circuit diagrams illustrate four different methods of wiring between a Pt 100 temperature sensor and its signal processing electronics. Which of the wiring methods gives the best measuring accuracy? \n\n1) Figure 4 \n\n2) Figure 2 \n\n3) Figure 3 \n\n4) Figure 1",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "In a distress situation, how many times or for how long should the emergency alarm signal be sounded? \n\n1) Until all crew members and passengers have reported to their respective muster stations \n\n2) 3 minutes \n\n3) 3 times \n\n4) Until the signal 'risk is over' or the order 'abandon ship' is given",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Following shows circuitry of a peak detector. What is the output voltage curve, Vo if Vi is a sinusoidal input curve? \n\n1) Vo will spike when Vi is at the maximum / minimum point of the sinusoidal curve; zero everywhere else \n\n2) Vo will peak at a level less than Vi maximum voltage and remain constant throughout \n\n3) Vo will be the same sinusoidal curve but at a lesser amplitude. \n\n4) Vo will peak when Vi is at the maximum, remain constant and fall to zero when Vi becomes negative",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)


        await add_question(test_id,
                           "Who is responsible for ensuring that your ship's security plan meets the requirements of the ISPS Code? \n\n1) Recognized Security Organization \n\n2) Ship Security Officer \n\n3) Company Security Officer \n\n4) Flag State Administration",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Give the meaning of the following symbol \n\n1) Survival craft distress pyrotechnic signals \n\n2) Survival craft portable radio \n\n3) Rocket parachute flare \n\n4) EPIRB",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "What is the likely cause of a decrease in the pH-value and an increase of the sulphate content of a diesel engine's cooling water system? \n\n1) Exhaust gas leakage into the cooling water system. \n\n2) Leakage from the lubricating oil coolers. \n\n3) Seawater leakage into the cooling water system \n\n4) Overdosing of corrosion inhibitor treatment chemicals",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "A ship's power system operates at 60Hz but when connected to shore supply it is supplied with 50Hz. Which of the following would you expect? \n\n1) Generators are more sensitive to reverse power faults. \n\n2) Electric motors will run at reduced speed and will tend to overload the magnetic structure of motor. \n\n3) Electric motors will run at increased speed and will tend to overload the magnetic structure of motor. \n\n4) Earth faults are more likely.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)


        await add_question(test_id,
                           "Which of the following temperature sensors normally gives the highest measuring accuracy? \n\n1) Thermocouple, NiCrNi \n\n2) Thermistor, PTC \n\n3) Resistance sensor, Pt100 \n\n4) Thermistor, NTC",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "How many Radar Transponders (SART) are required to be carried onboard a ship for use in survival crafts? \n\n1) 2, one of which being capable of floating free if the ship sinks \n\n2) One in each lifeboat \n\n3) Two on each side of the ship \n\n4) One on each side of the ship",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "The turbocharger on a diesel engine is surging and making occasional, loud 'whoofing' noises. Which one of the options given is the most probable cause of this? \n\n1) Rapid changes in engine load due to rough sea conditions. \n\n2) Exhaust system recently cleaned. \n\n3) Engine on bridge control. \n\n4) Air leakage from scavenge receiver.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "For a large 2-stroke diesel engine, what would be a typical set point for the low pressure shut down for the lubricating oil inlet to the main bearings? \n\n1) 10.0 bar \n\n2) 1.0 bar \n\n3) 5.0 bar \n\n4) 0.1 bar",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)


        await add_question(test_id,
                           "The typical current gain for a common emitter transistor is \n\n1) One to Tens \n\n2) One to Thousands \n\n3) Tens to Hundreds \n\n4) Hundreds to Thousands",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "How often are 'abandon ship' drills required to be held on cargo vessels according to SOLAS? \n\n1) Once every week. \n\n2) Once every year. \n\n3) Once every 6 months. \n\n4) Once every month.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "The muster list must be prepared: \n\n1) At any moment before the ship proceeds to sea \n\n2) at least 2 hours after the ship has proceeded to sea \n\n3) at least 2 hours before the ship proceeds to sea \n\n4) at least 1 hour before the ship proceeds to sea",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Which personnel must undergo familiarization training on board \n\n1) Only catering staff \n\n2) Everyone \n\n3) Only the ratings \n\n4) Only the deck officers",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)


        await add_question(test_id,
                           "Which one of the following is not a requirement of an emergency generator used onboard ship? \n\n1) Driven by prime mover with an independent supply of fuel \n\n2) Connected automatically to the emergency switchboard in not more than 45 second \n\n3) Connected automatically when first main generator is overloaded \n\n4) Started automatically upon failure of main source of electrical power supply",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Identify symbol shown below. \n\n1) Motor \n\n2) Solenoid \n\n3) Spring \n\n4) Diaphragm",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "In terms of automated control systems, what is applicable for a continuous control system? \n\n1) Automatic control in which the controlled quantity is measured continuously and corrections are a continuous function of the deviation \n\n2) The control valve will always be changing position \n\n3) It is not possible to have a stable process \n\n4) The output signal is equal to the input signal",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "When two alternators are operating in parallel and field current of the second alternator is increased, which of the following is not observed? \n\n1) Reactive power supplied by second alternator is increased \n\n2) Apparent power supplied by first alternator is increased \n\n3) Reactive power supplied by first alternator is decreased \n\n4) System terminal voltage is increased",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)


        await add_question(test_id,
                           "Ordinary thyristors (SCR) must often be protected against reverse overvoltage transients. This is because they can be damaged by over-voltage, even if it is of extremely short duration. These SCRs have been given such over-voltage protection, but only one of them is correct. Which one is it? \n\n1) Figure 3 \n\n2) Figure 4 \n\n3) Figure 1 \n\n4) Figure 2",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Which organization or administration is responsible for surveys and inspections of ships, and the issue of Safety Certificates? \n\n1) Government Authorities of the Flag State \n\n2) Ships Classification Associations (Lloyd's, American Bureau of Shipping, The Norwegian Veritas, Germanische Lloyd's, etc.) \n\n3) International Labor Organization (ILO) \n\n4) International Maritime Organization (IMO)",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "What percentage of the baggage is required to be checked at Security Level 1? \n\n1) 5-15% of the baggage is required to be checked at Security Level 1. \n\n2) 25-50% of the baggage is required to be checked at Security Level 1. \n\n3) 100% of the baggage is required to be checked at Security Level 1. \n\n4) The percentage is not specified.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "For how long is the health certificate valid for a seafarer above the age of 18? \n\n1) One year. \n\n2) Two years. \n\n3) Three months. \n\n4) No time limit.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)


        await add_question(test_id,
                           "The correct order of actions to be taken in a fire emergency, should be... \n\n1) Extinction, evaluation of the situation, confinement of fire, rescue and life-saving \n\n2) Evaluation of the situation, confinement of fire, rescue and life-saving, extinction \n\n3) Evaluation of the situation, rescue and life-saving, confinement of fire, extinction, then feed back on the emergency \n\n4) Extinction, confinement of fire, feed back on the emergency, rescue and life-saving, then evaluation of the situation",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "MARPOL - Annex IV. Prevention of Pollution by Sewage from ships. What do you understand by the word 'Sewage'? \n\n1) Waste from synthetic materials. \n\n2) Waste from galley. \n\n3) Mixture of sea water/oil. \n\n4) Drainage/waste from toilets/urinals.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "You are on board a cargo ship. The ship is heavily listing to starboard, making impossible the launching of the survival craft stowed on this side. Lifeboats and liferafts are equally distributed on each side of the vessel. What should be the total number of persons that can be accommodated in the remaining survival craft stowed on the port side? \n\n1) at least 200 % N (lifeboat capacity: 100 % N; liferaft capacity: 100 % N) \n\n2) at least 150 % N (lifeboat capacity: 50 % N; liferaft capacity: 100 % N) \n\n3) at least 150 % N (lifeboat capacity: 100 % N; liferaft capacity: 50 % N) \n\n4) at least 100 % N (lifeboat capacity: 50 % N; liferaft capacity: 50 % N)",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Give the meaning of the following symbol \n\n1) Survival craft distress pyrotechnic signals \n\n2) Rocket parachute flares \n\n3) Line throwing appliance \n\n4) Parachute landing area",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)


        await add_question(test_id,
                           "The Training Manual shall contain instructions and information on the life-saving appliances and the best method of survival. The training manual shall contain detailed explanations of crew duties in relation to emergency situations. Which of the following tasks or duties shall be included in the manual according to present regulations? \n\n1) The use of surface to air visual signals to be used by survivors. \n\n2) The use of escape routes and other escape methods. \n\n3) The use of the ship's line throwing apparatus. \n\n4) The use of navigational equipment for survival crafts.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "What would be the preferred colour to use when maintaining the paint on shell, plating, structure and bottom/tanktopp in the engine room? \n\n1) Dark brown/red colour to camouflage any minor leakages and oil spills. \n\n2) Whatever paint is available. \n\n3) The same colour as machinery and equipment. \n\n4) White or light grey to ensure all minor spills and leakages are noticed and dealt with.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Which of the following is true of the reed switch? \n\n1) Low on-resistance. \n\n2) Low reliability \n\n3) High off-resistance \n\n4) Low offset voltage",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "What does the term DISCHARGE mean, as used in the Oil Pollution Regulations? \n\n1) Spilling \n\n2) All the other alternatives \n\n3) Leaking \n\n4) Dumping",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)


        await add_question(test_id,
                           "What effect would turbulent fluid flow through a heat exchanger have on the efficiency of the heat transfer? \n\n1) Turbulent fluid flow generally reduces heat transfer efficiency \n\n2) Heat transfer efficiency is not affected by the type of fluid flow through the heat exchanger. \n\n3) Turbulent fluid flow generally increases heat transfer efficiency. \n\n4) It cannot be determined since it is not possible to generate turbulent fluid flow through a heat exchanger?",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "A fluorescent lamp is found to be flicking rapidly. What is the possible cause? \n\n1) Arc suppresser contacts are shortened \n\n2) Normal ageing of lamp \n\n3) Short-circuit on light fitting \n\n4) Loss of active material or fracture at one electrode",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "During operation of the main engine, the exhaust temperature increases on one of the cylinders. The turbocharger starts surging and smoke is seen coming out from the turbocharger inlet air filter. What is the most probable cause? \n\n1) Scavenge box fire \n\n2) High back pressure in the exhaust system after the turbocharger. \n\n3) A fuel valve is stuck in the open position. \n\n4) Turbocharger failure.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "What does the term 'stoichiometric mixture' mean when used in relation to combustion of hydrocarbon fuels? \n\n1) A ideal mixture of fuel and air in which all of the oxygen in the air in the mixture is consumed during combustion. \n\n2) An ideal mixture of fuel and air in which all of the fuel and oxygen in the mixture are consumed during combustion. \n\n3) A ideal mixture of fuel and air in which all of the fuel in the mixture is consumed during combustion. \n\n4) An ideal mixture of fuel and air in which all of the fuel in the mixture is consumed during combustion with a minimum of excess air.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)


        await add_question(test_id,
                           "Where is shunt motor normally used? \n\n1) Where varying speed is desired regardless of load \n\n2) Where higher starting torque and varying speed is desired \n\n3) Where uniform speed is desired regardless of load \n\n4) Where low starting torque is desired",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "The emergency fire pump is in accordance with good seamanship and precautionary routines run and tested weekly. Routine checks and maintenance are normally carried out by dedicated personnel. To ensure safe and appropriate operation of the pump, would you consider it beneficial that the same dedicated personnel operate the pump in emergencies? \n\n1) In case of accidents, it is important that a wide range of personnel must be permitted and trained to operate the pump. \n\n2) Only senior deck officers should operate the emergency pump. \n\n3) Only senior engineers should operate the emergency pump. \n\n4) To ensure safe operation of the emergency pump, only dedicated personnel must be permitted to operate the pump.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "OPA-90 is referring to a Qualified Individual (QI). \n\n1) QI is the owner's contingency leader \n\n2) An individual certified by USCG to handle oil spills \n\n3) QI is representing the USCG \n\n4) QI is an authorised individual, situated in the US, and contracted by the owner or operator of the vessel",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "If drugs or suspected drugs are found onboard your ship, follow the five C's. Confirm, Clear, Cordon, Control and: \n\n1) Chuck \n\n2) Check \n\n3) Cheer \n\n4) Change",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)


        await add_question(test_id,
                           "Which statement about the use of profiling onboard a ship is true? \n\n1) Profilers need at least half an hour to gather the information they need. \n\n2) Only visitors can be profiled. \n\n3) A random selection process must be established. \n\n4) Detection equipment can be used in place of profiling.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "With reference to piping and instrumentation diagram (P&ID), what does below symbol represent? \n\n1) Motor \n\n2) Filament lamp \n\n3) Anti-condensation heater \n\n4) Heat exchanger",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Which of these tasks are performed as part of the SSA? \n\n1) Assess the likelihood and potential consequences of security incidents. \n\n2) Assign security duties to ship personnel. \n\n3) Train shipboard personnel in their security duties. \n\n4) Implement measures to address weaknesses in ship security.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "MARPOL - Annex V. Disposal of garbage. Your vessel is in the Red Sea (Special Area) and the Chief Cook is requesting to have some food waste burned in the incinerator. Due to problems with incinerator, you decide to have the waste ground in the Grinder (Lump size max. 25 mm) and disposed off into the sea. Is this prohibited, if not, how far from nearest land is this legal? \n\n1) 3 miles \n\n2) 12 miles \n\n3) This is prohibited \n\n4) 25 miles",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)


        await add_question(test_id,
                           "What does the term OIL mean, as used in the Oil Pollution Regulations? \n\n1) Oil refuse \n\n2) Fuel oil \n\n3) All of the mentioned \n\n4) Sludge",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Who is the leader of the lifeboat drill (abandon ship drill)? \n\n1) Sen.Off.Deck. \n\n2) The first member of the crew arriving at the survival craft. \n\n3) Sen.Off.Engine. \n\n4) The appointed lifeboat commander.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "The pressure delivered by a gear type fuel oil transfer pump suddenly reduces from 5 bar to 4 bar during transfer. From the options given, select the most likely cause of this occurrence. \n\n1) Part of the pump relief/recirculation valve spring has broken off allowing the valve to open further. \n\n2) The pump drive has sheared. \n\n3) The oil tank from which the oil is being transferred is empty. \n\n4) The pump gears and casing have become worn.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Which of this information must be included in a piracy attack alert? \n\n1) The number of pirates/highjackers. \n\n2) Your ship's name and call sign. \n\n3) The number of crew onboard. \n\n4) The type of weapons being carried by the pirates/highjackers.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)


        await add_question(test_id,
                           "As a minimum, how often shall life boats be launched with their assigned operating crew aboard and manoeuvred in the water according to SOLAS? \n\n1) Every month. \n\n2) Every two weeks. \n\n3) Every three months. \n\n4) Every week.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Which international convention deals with pollution prevention? \n\n1) ISGOTT. \n\n2) STCW. \n\n3) SOLAS. \n\n4) MARPOL.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "What is the r.p.m. of a 4-pole motor operating at 60Hz? \n\n1) 1800 r.p.m. \n\n2) 1500 r.p.m. \n\n3) 3600 r.p.m. \n\n4) 1200 r.p.m.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "How is the prime mover load normally kept to a minimum when starting up an electric driven reciprocating type air compressor? \n\n1) By using an unloading device to keep the compressor suction valves open until the machine is up to speed. \n\n2) By keeping the second stage drain valve open until the machine is up to speed. \n\n3) By using an unloading device to keep the compressor delivery valves open until the machine is up to speed. \n\n4) By keeping the main discharge valve closed until the machine is up to speed.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "A transformer overheats while taking a shore supply. Which is the likely cause? \n\n1) Incorrect earthing \n\n2) Incorrect frequency \n\n3) Incorrect voltage \n\n4) Incorrect current",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Some process control systems may have several inputs and controlled variables. In this context what is meant by split-range? \n\n1) Several controllers are connected to the same control-valve \n\n2) Several control-loops for the same range \n\n3) Several control-valves are connected to the same controller \n\n4) On-Off control",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "What is the period of validity of the Safety Management Certificate \n\n1) 2 years \n\n2) 6 months \n\n3) 1 Year \n\n4) 5 years",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "A cable has a resistance of 100 milli-ohms. It supplies a 300A load over a distance of 100 metres. What is the voltage drop along it's length? \n\n1) 30 volts \n\n2) 300 volts \n\n3) 3.0 volts \n\n4) 300 milli-volts",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "A Multimeter is not suitable to measure \n\n1) Resistance \n\n2) Power \n\n3) Voltage \n\n4) Current",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "When carrying out routine insulation testing of a three-phase induction motor, which of the measurement should be covered? \n\n1) U-V-W-E \n\n2) U1-U2, V1-V2, W1-W2, U-E, V-E, W-E \n\n3) U-E, V-E, W-E, U-V, V-W, W-U \n\n4) AA-E, ZZ-E",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Most fuel oil separators working on the centrifuge principle have an automatic start up and sludging facility. Which of the following actions would you expect to occur first during the start-up sequence? \n\n1) Operating water supplied to bowl to close it \n\n2) Sealing water supplied to bowl to prevent carry over \n\n3) Fuel oil supplied to bowl to fill it \n\n4) Operating water drained from bowl to open it.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The fuel consumption for the main diesel engine has gradually increased over a period of a few months. All system pressures and temperatures appear normal. From the options given, choose the one which is the most likely cause of this. \n\n1) Damaged propeller blade \n\n2) Fouling of the hull \n\n3) Sea water temperature changing \n\n4) Water in the fuel.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)


        await add_question(test_id,
                           "Which one of the following items has to be included in an abandon ship drill according to SOLAS regulations? \n\n1) Starting and operating radio life-saving appliances. \n\n2) Manoeuvring the lifeboat in the water. \n\n3) Checking that life-jackets are correctly donned. \n\n4) Launching and recovery of a survival craft.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "In a PID controller the setting of the Proportional band (P), the Reset time (I) and the Rate time (D) may be adjusted. Please indicate which curve shows the typical response to a change in input, if the setting of the proportional band is too wide. \n\n1) Figure 3. \n\n2) Figure 2. \n\n3) Figure 4. \n\n4) Figure 1.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "When selecting switchgear to work with High Voltage it is important to use an appropriate arc quenching medium. What is meant by arc quenching medium? \n\n1) The gas, liquid or vapour which will minimise creation of an electric arc as contacts open. \n\n2) The way in which the contacts separate as the switchgear operates. \n\n3) Equipment which communicates information about the arcing. \n\n4) A material which assists a welding process.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "An actuator has 'loose linkage' with the valve stem. What is the result output from the controller to identify the problem? \n\n1) Compound curve \n\n2) Process Cycling \n\n3) Linear curve \n\n4) Step curve",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)


        await add_question(test_id,
                           "MARPOL - Annex I. Your vessel sailed from Bahrain heading for Singapore. 2 days after departure, you would like to empty your machinery space bilges. What will be the correct procedures in this connection? \n\n1) Call the bridge and request for position and permission to discharge overboard through oily water separating and filtering equipment. \n\n2) Discharge overboard through oily-water separating and filtering equipment without calling the bridge. \n\n3) Call the bridge and request for position and permission to discharge directly overboard. \n\n4) Wait till after darkness and discharge in most convenient way.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "A compressed air supply system has two automatically controlled air compressors. When demand is high both compressors are needed to meet the delivery requirements. What is the best method for controlling the compressors to meet a varying, but intermittent demand? \n\n1) Sequential start initiated by pressure switches set at different switching pressures. \n\n2) One compressor running continuously with the other on standby. \n\n3) Continuous running of both compressors and the use of unloading devices. \n\n4) Start and stop of the compressors controlled by timer switches.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "HEL-H is the abbreviation of a heavy helicopter radius of action for rescue purposes. What do you think the radius and evacuating capacity of the helicopter is? \n\n1) 150 nm and capacity for evacuating more than 12 persons. \n\n2) 100 nm and capacity for evacuating more than 10 persons. \n\n3) 200 nm and capacity for evacuating more then 15 persons. \n\n4) 500 nm and capacity for evacuating more than 25 persons.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "When a vessel violates the oil pollution laws, who may be held responsible? \n\n1) Captain only \n\n2) Shipowners only \n\n3) Officers only \n\n4) Any one involved in the operation",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)


        await add_question(test_id,
                           "Which of the options given is the most likely reason for a drop in pressure at the charge air manifold of a diesel engine? \n\n1) Air filter to turbocharger fouled or obstructed. \n\n2) Charge air cooler fouled on waterside \n\n3) Air passageways or ports to the engine cylinders partly blocked due to fouling. \n\n4) Increased engine load.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Searches are often triggered by: \n\n1) News stories of stowaways. \n\n2) An increase in security level by the Flag State. \n\n3) The receipt of a shipment of damaged stores. \n\n4) Lost baggage.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "The main engine is running steady with an average exhaust gas temperature of approximately 350°C. What would be a typical alarm/slow down setting for the cylinder exhaust gas temperature deviation from the average? \n\n1) +/- 30°C \n\n2) +/- 80°C \n\n3) +/- 50°C \n\n4) +/- 10°C",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "What does term 'precision' mean? \n\n1) Nearness to which true value is measured \n\n2) An input is repeatedly applied for short time intervals under fixed conditions. \n\n3) Average of deviations from the desired outputs tends to zero or is zero itself \n\n4) Applied number of occasions where an instrument indicates readings which are very close in value",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)


        await add_question(test_id,
                           "A controller was idle for 10 seconds. The controller output change at the 25th second. The process variable started to change at the 50th second. What is the dead time? \n\n1) 25 seconds \n\n2) 85 seconds \n\n3) 35 seconds \n\n4) 15 seconds",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Why is it important to reduce the diesel engine load during in service water washing of the turbocharger gas side? \n\n1) To prevent overload of the turbocharger bearings. \n\n2) To prevent damage to the turbine blades \n\n3) To reduce the air pressure to the water dosage pot. \n\n4) To avoid cold corrosion of exhaust system.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "What would happen if, when a ship is undergoing a Port State Inspection, certificates were invalid or missing \n\n1) The deficiencies would be recorded in the ship's register and the ship allowed to sail \n\n2) The ship would be allowed to sail to the next port and rectification would take place then \n\n3) Rectification would be required before sailing \n\n4) The ship would be detained indefinitely",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Give the meaning of the following symbol \n\n1) Rocket parachute flares \n\n2) Parachute landing area \n\n3) Survival craft distress pyrotechnic signals \n\n4) Line throwing appliance",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)


        await add_question(test_id,
                           "Which IMO convention takes care of the human safety at sea? \n\n1) The SOLAS convention \n\n2) the STCW 78/95 \n\n3) the MARPOL convention \n\n4) there isn't any conventions that take care of the human safety at sea",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "MARPOL - Annex IV. Your ship has in operation an approved sewage treatment plant certified by the Administration. During discharge, while vessel is awaiting pilot off Cape Henry, USA, the surrounding water is discoloured. What kind of action would be appropriate to take? \n\n1) Continue discharge since the treatment plant is of an approved type. \n\n2) Stop discharge. \n\n3) Reduce discharge rate in order to have less discolouration of surrounding water. \n\n4) Continue discharge since Annex IV of MARPOL is internationally not yet in force.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "This figure shows a transformer, with two windings, N(1) = 2000 and N(2) = 1000 turns, on a common magnetic circuit. Assume that there is no energy loss in the transformer itself. Calculate the current I(2) when the current I(1) = 2 A. \n\n1) I(2) = 8 A \n\n2) I(2) = 1 A \n\n3) I(2) = 4 A \n\n4) I(2) = 2 A",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "What is the minimum number of channels required for the portable two-way VHF's for survival craft? \n\n1) Channels 6, 12 & 16 \n\n2) Channel 16 only \n\n3) Channels 16 & 12 \n\n4) Channels 6, 13 & 16",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)


        await add_question(test_id,
                           "Why is it important to have good relationship on-board a vessel? \n\n1) It leads to better work performance and positive atmosphere among the crew \n\n2) Crew comes to know each others problems \n\n3) It will prevent accidents from happening \n\n4) It encourages crew to extend their contract",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Which of the following is not true of the photo resistor? \n\n1) Very low offset voltage \n\n2) High switching rate capability \n\n3) High on-resistance \n\n4) Moderate off-resistance",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "What is the minimum number of portable two way VHF walkie talkies for use in survival craft, that should be carried onboard vessels which comply with GMDSS regulations? \n\n1) There is no requirement to carry them. \n\n2) 1 set \n\n3) 3 sets \n\n4) 2 sets",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "When a Master takes the leadership in approaching a problem, Must his first action be a decision that will directly solve the problem? \n\n1) Not necessary, he shall use all available resources. He should resist the temptation to step in and do it all by himself \n\n2) No, he should observ the situation, and let the other senior officers solve the situation. \n\n3) Yes, take full controll. Do not delegate to other officers, to avoid mistake. \n\n4) Yes, with his experience, it is most likely that he has the best solution.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "Which of the following test results obtained using a Digital Multi-Meter shows that a diode is in good working condition? \n\n1) With + to Anode a reading of about 0.6V and with probes reversed a reading of O/L. \n\n2) With + to Cathode a reading of about 0.6V and with probes reversed a reading of O/L. \n\n3) With + to Anode good continuity (low ohms) and with the probes reversed a reading of infinity. \n\n4) With + to Cathode good continuity (low ohms) and with the probes reversed a reading of infinity.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "During inspection of the crank bearing for one of the units in the main engine, the bearing shell was found as follows: Surface of the white metal was black and very hard. Patches of black incrustations have worn grooves in the journal. What is the likely cause of this condition? \n\n1) Dirt particles in the lubricating oil during service. \n\n2) Bearing shell service time exceeded. \n\n3) Poor casting of bearing shell white metal lining. \n\n4) Water present in the lubricating oil during service.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Your ship security plan must include procedures for responding to security threats, auditing security activities and interfacing with the port facility. \n\n1)  \n\n2) TRUE\n\n3) \n\n4) FALSE",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)


        await add_question(test_id,
                           "Which of the following items shall be included in an abandon ship drill? \n\n1) Checking passenger's immersion suits \n\n2) Checking the distress signal rockets and other distress signals \n\n3) Instruction in the use of radio life-saving appliances \n\n4) Checking the lifeboat provisions and supplies",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)


        await add_question(test_id,
                           "Select, from the options given, the one most likely to result in a sudden reduction in main diesel engine operating speed during normal operation. \n\n1) Fuel oil pipes or filters becoming fouled. \n\n2) Leaking exhaust valves. \n\n3) Bad fuel oil quality. \n\n4) Loss of signal to engine governor.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "As per SOLAS regulations, the general emergency alarm system must be tested: \n\n1) Every week \n\n2) Every 2 weeks \n\n3) Every month \n\n4) Every 3 weeks",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Temperatures are often measured by using platinum resistance thermometers. The characteristics shown are all calibration curves for such devices. Which of them is a calibration curve for a PT100 sensor? \n\n1) Figure 3 \n\n2) Figure 1 \n\n3) Figure 2 \n\n4) Figure 4",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "What does ISM stand for? \n\n1) Internal Ship Safety Management \n\n2) International Safe Manning Certification \n\n3) The International Management Code for the Safe Operation of Ships and for Pollution Prevention \n\n4) International Ship Measurement and Pollution Control",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)


        await add_question(test_id,
                           "Which of the following is an application of an capacitive sensor? \n\n1) Barometer \n\n2) Tachometer \n\n3) Piezoelectric sensor \n\n4) Proximity sensor",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "\"Protective discrimination\" means the progressive grading of sizes or tripping times of: \n\n1) Line fuses and overcurrent relays \n\n2) 440 V and 220 V transformers. \n\n3) Magnetic and thermal current transformers. \n\n4) Generators and motors.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "How often shall crew members participate in fire drills? \n\n1) Once every 6 months \n\n2) Once every month \n\n3) Once every year \n\n4) Once every week",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "What should you do with the ashes from your vessels incinerator which had burned garbage containing plastics? \n\n1) Discharge at sea providing you are not in any river or estuary \n\n2) Discharge at sea providing you are more than 25 miles offshore \n\n3) Discharge to a shore facility only \n\n4) Discharge at sea providing you are more than 12 miles offshore",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)


        await add_question(test_id,
                           "A Cargo Ship Equipment Certificate will be issued for: \n\n1) 2 years with control every 6 months \n\n2) 4 years \n\n3) 3 years \n\n4) 5 years with control every 12 months",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Any ship of 10.000 tons gross tonnage and above shall be fitted with oily-water separating equipment for the control of machinery space bilges. What kind of equipment is required in this connection? \n\n1) Either Oil filtering equipment, or Oily-water separating equipment, or combination of both. \n\n2) Oil filtering equipment only. \n\n3) Sludge separating tank. \n\n4) Oily-water separating equipment only.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "How do you change the below earth neutral system into an isolated neutral system? \n\n1) Replace link with fuse \n\n2) Remove earth on generator neutral \n\n3) Remove all earthing lead \n\n4) Cannot be done",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "What is the function of a Spectrum Analyzer? \n\n1) Outputs the voltage wave of the signal \n\n2) Measures complex impedance of network at varying frequencies \n\n3) Informs the frequency spectrum of the signal \n\n4) Measures and displays the frequency characteristic",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)


        await add_question(test_id,
                           "Temperature sensors of all types are normally mounted in a well, or pocket, when used in pipelines. Why is this done? \n\n1) Allow removal of the sensor also when liquid is flowing in the pipe. \n\n2) Decrease the temperature gradient between the liquid and the sensor. \n\n3) Avoid electric current flowing from the sensor to the liquid. \n\n4) Suppress electro-magnetic interference between liquid in the pipe and the sensor.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Who is responsible for keeping the required official publications onboard? \n\n1) The authorities. \n\n2) The radio officer. \n\n3) The owner. \n\n4) The master.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Which one of the following is not an electronic switch? \n\n1)  MOSFET \n\n2) Thermocouple \n\n3) Bipolar Transistor \n\n4) Thyristor",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "New MARPOL regulations came into effect from July 93 stating that the previous instantaneous rate of discharge of oil content (60 litters per nautical mile) was changed to: \n\n1) 30 litters per nautical mile \n\n2) 25 litters per nautical mile \n\n3) 20 litters per nautical mile \n\n4) 10 litters per nautical mile",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "Who is responsible for issuing an ISPS certificate? \n\n1) The insurance company \n\n2) US Coast Guard \n\n3) The Flag State \n\n4) The Port State",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Which of these conventions is The International Ship and Port Facility Security (ISPS) Code a part of? \n\n1) The Anti Terrorist International Agreement \n\n2) STCW-95 \n\n3) MARPOL \n\n4) SOLAS",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "What are the conditions that influence the efforts for organising the fire fighting? \n\n1) Where the fire breaks out, how many fire teams are available, the strength of the fire, the ships mobility, what is burning and communication \n\n2) Where the fire break out, the ships mobility, distance to the fire station and the size of the fire brigade \n\n3) Where the fire break out, how many fire teams are available, what is burning, distance to the fire station \n\n4) Distance to the fire station and the size of the fire brigade, what is burning, possibility to get water",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "During abandon ship exercise, what life-saving equipment must be demonstrated? \n\n1) Lifeboat radio \n\n2) Wearing and fastening of lifejackets and associated equipment \n\n3) Location of immersion suits and thermal protective aids \n\n4) How to communicate using the hand-held radios",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)


        await add_question(test_id,
                           "Which device does this graphical symbol illustrate? \n\n1) Differential pressure transmitter \n\n2) Rectifier \n\n3) Pressure to current converter \n\n4) Inverter",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Which international organization is preparing conventions and rules for seafaring nations? \n\n1) International Marine Association (IMA) \n\n2) International Ocean Safety Organization (IOSO) \n\n3) International Labor Organization (ILO) \n\n4) International Maritime Organization (IMO)",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "What would be the most probable cause if the exhaust gas from a diesel engine looked a bit blue in colour? \n\n1) Engine burning too much lubricating oil \n\n2) Bad fuel oil \n\n3) Blocked charge air cooler \n\n4) Engine is too cold",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "A 6-Volt dc relay is to be used with a 12-Volt power supply. The relay requires a current of 0.1 Amp. What is the series resistance required. \n\n1) 480 ohm  \n\n2) 60 ohm\n\n3) 80 ohm \n\n4) 120 ohm",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)


        await add_question(test_id,
                           "In process control some situations lead to a need for dynamic amplifying. What is meant by dynamic amplifying? \n\n1) Amplitude of input signal divided by amplitude of output signal \n\n2) Corresponding change in signals \n\n3) Amplitude of output signal divided by amplitude of input signal \n\n4) Variable amplifying",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Which of following are security duties? \n\n1) Checking ID of visitors onboard \n\n2) Monitoring of restricted areas \n\n3) Calibration of security equipment \n\n4) All alternatives",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Why shall a duly qualified officer supervise any potential polluting operation? \n\n1) To avoid pollution \n\n2) To inform the authorities \n\n3) To restrict pollution \n\n4) To relieve the master",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "What is the status of the rules of the SOLAS convention? \n\n1) Supplementary to classification rules \n\n2) Mandatory \n\n3) Must be regarded as guidelines \n\n4) Should be consulted when the vessel is in distress",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)


        await add_question(test_id,
                           "What is the effect of noise on any electronic system? \n\n1) Limits the bandwidth of the measurement system \n\n2) Limits the reliability of the measurement system \n\n3) Limits the accuracy of the measurement system \n\n4) Limits the precision of the measurement system",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Which of the following locations are lightings not required to be supplied from emergency power for period of 18 hrs? \n\n1) Steering gears \n\n2) Emergency fire pump room \n\n3) Service and accommodation alleyways \n\n4) Galley",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "In which of the following automated control processes will the time constant be of minor importance? \n\n1) Flow control \n\n2) Level control \n\n3) Pressure control \n\n4) Temperature control",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "You are onboard a vessel off the West African coast. You want to dump a mixture of food waste, glass bottles and floating packing materials. Is this allowed and if so, how far off the coast would you have to be? \n\n1) This is prohibited \n\n2) 12 nautical miles off the coast \n\n3) 3 nautical miles off the coast \n\n4) 25 nautical miles off the coast",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "In the context of an automated control system, which controller must be tuned first in a cascade control system? \n\n1) The primary controller \n\n2) Any one of them \n\n3) The secondary controller \n\n4) Both at the same time",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Which information should be included in your search plan? \n\n1) Known hiding spots to be searched. \n\n2) Areas to be searched. \n\n3) Personnel to be involved in the search. \n\n4) Areas to be searched and personnel to be involved in the search.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Which ships does the ISM code apply to \n\n1) All passenger ships, all cargo ships of 500GRT or above \n\n2) Only passenger vessels \n\n3) Only tankers and Ro-ros \n\n4) All craft above 300GRT",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "What is meant by Ingress protection \"IP56\"? \n\n1) Dust tight, protected against submersion \n\n2) Dust protected, protection against heavy seas \n\n3) Dust tight, protected against water jets from all direction \n\n4) Non protected against any solid objects or dust, protected against heavy seas",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)


        await add_question(test_id,
                           "When considering instrumentation systems, what is meant by static sensitivity? \n\n1) Corresponding change in signals \n\n2) Change in input signal times change in output signal \n\n3) Change in output signal divided by change in input signal \n\n4) Change in input signal divided by change in output signal",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Which of the following duties shall be included in the \"muster list\" as being assigned to members of the crew? \n\n1) Operation of the vessel's propulsion system \n\n2) Preparation of immersion suits for the ship's passengers \n\n3) Preparation of manoeuvres intended to ease launching of the survival craft \n\n4) Preparation and launching of the survival craft",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Where is the Safety Certificates for ships to be kept? \n\n1) In the Captain's office \n\n2) Posted up in a prominent place onboard the ship \n\n3) In the Owner's office \n\n4) In the Captain's safe",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "A smart transmitter is suspected to be faulty. A few steps need to be taken to assess the functionality of the transmitter. Which of the following is not one of the steps? \n\n1) Check the calibration \n\n2) Check the precision \n\n3) Check the filering \n\n4) Check the configuration",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)


        await add_question(test_id,
                           "One of the categories of information that must be included in your SSP is: \n\n1) Ship security survey \n\n2) Threat scenarios \n\n3) Security arrangements \n\n4) Weaknesses in security measures",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "New MARPOL regulations came into effect from July 93 stating that the oily water separator which was previously certified for 100 ppm be changed to: \n\n1) 25 ppm \n\n2) 50 ppm \n\n3) 10 ppm \n\n4) 15 ppm",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "In which areas is plastic material accepted for overboard disposal? \n\n1) Not permissible anywhere. \n\n2) In coastal waters. \n\n3) 100 n.m. from shore line. \n\n4) In specially designated areas (ref. MARPOL).",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Who is responsible for ensuring your ship completes a security assessment? \n\n1) Flag State Administration \n\n2) Company Security Officer \n\n3) Ship Security Officer \n\n4) Recognized Security Organization",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)


        await add_question(test_id,
                           "What manoeuvre should be carried out in case of a fire onboard a ship? \n\n1) Keep the stem up against the wind if possible \n\n2) Continue on course and speed \n\n3) Reduce speed and, if possible, keep the fire zone to the leeward of the ship \n\n4) Let the ship follow the wind in order to reduce the oxygen supply",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "The figure shows a silicon controlled rectifier with a RC circuit connected in parallel. What is the purpose of the RC circuit? \n\n1) Provide a controlled time delay for the SCR trigger pulse. \n\n2) Measuring the current through the SCR \n\n3) Obtain current resonance \n\n4) Protect the SCR against damage caused by fast high voltage spikes",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "In a distress situation and immediately after the distress signal has been sounded, what is the next action to be taken by the Chief Officer on duty? \n\n1) Use the intercom to inform crew and passengers of the reason for the alarm \n\n2) Use the VHF-radio telephone to ask ships in the vicinity to stand by \n\n3) Send distress signals to call for help \n\n4) Call the nearest coastal radio station",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "In a closed loop process control of a valve, oscillations has been found in the output of the controller. What is the probable cause? \n\n1) Control gain is too small \n\n2) Stiction in the valve \n\n3) Improperly calibrated valve \n\n4) Loose connections in the control loop",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)


        await add_question(test_id,
                           "Which of these statements about profiling is correct? \n\n1) Check the ID of all visitors and some crew prior to boarding. \n\n2) Use only open-ended questions. \n\n3) Verify that answers to questions match up with what's already known about the person being questioned. \n\n4) Pay less attention to body language and behaviour and more attention to answers to questions.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Check the items that can be a possible threat \n\n1) Bombing and Sabotage \n\n2) 'Piracy, Hijacking and Smuggling' \n\n3) Cargo tampering and Stowaways \n\n4) All alternatives",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Below shows a typical shore supply connection box. What does device SSA stand for? \n\n1) Sequence supply available lamp \n\n2) Shore supply available lamp \n\n3) Ship supply available lamp \n\n4) Switchboard supply available lamp",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Poster or signs shall be provided on or in the vicinity of survival craft and their launching controls. Which one of the following requirements has to be included? \n\n1) Give information on survival craft capacity \n\n2) Give an overview of location of all lifesaving appliances \n\n3) Give relevant instructions and warnings \n\n4) Give information on survival craft speed and seaworthiness",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)


        await add_question(test_id,
                           "Which PPM is allowed for discharging of 'Bilge Water' overboard? \n\n1) 50 PPM \n\n2) 100 PPM \n\n3) 0 PPM \n\n4) 15 PPM",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "A two step controller (open/close) has failed and the only available spare controller is a P+I controller. Select, from the options given, how the P+I controller could be set up to achieve approximate two step control. \n\n1) Set the proportional band to minimum width and the integral action to maximum (repeats per minute). \n\n2) Set the proportional band to maximum width and the integral action to minimum (repeats per minute). \n\n3) Set the proportional band to maximum width and the integral action to maximum (repeats per minute). \n\n4) Set the proportional band to minimum width and the integral action to minimum (repeats per minute).",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "For some time the remote reading temperature gauge for the meat room has been reading a higher temperature than the local liquid in glass thermometer. When removed and tested the remote gauge is found to be reading accurately. Which of the options given is the most likely cause of this discrepancy? \n\n1) The sensing bulb for the remote gauge is placed in a relative 'local hot spot' inside the meat room. \n\n2) The liquid in glass thermometer is positioned in a relative cold spot in the meat room. \n\n3) The liquid in glass thermometer is reading incorrectly. \n\n4) The lagging for the capillary tube from the sensing bulb to the temperature gauge outside of the meat room is too thick causing the tube to heat up.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Temperature sensors may be marked PT100. What does this mean? \n\n1) 100 ohm at 20°C \n\n2) 100 ohm at 0°C \n\n3) 20 ohm at 100°C \n\n4) 0 ohm at 100°C",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)


        await add_question(test_id,
                           "Who is responsible for completing the DoS on behalf of the ship? \n\n1) Chief Engineer \n\n2) Chief Officer \n\n3) Ship Security Officer \n\n4) Company Security Officer",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "The best way to prevent stowaways from boarding your ship is to: \n\n1) 'Seal spaces that are not in use while in port, and perform a search of the ship before leaving.' \n\n2) Conduct a Nominated Officers search. \n\n3) Search the ship when you arrive at port and again just after leaving. \n\n4) 'Conduct routine, but irregular searches of the ship.'",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "You are on a vessel 10 nautical miles off the coast of Nigeria, West Africa. Are you allowed to dump empty glass bottles overboard? \n\n1) No, glass bottles cannot be dumped overboard \n\n2) Yes, the bottles can be dumped if they are ground so that the resulting particles can pass through a screen with 50 mm openings \n\n3) Yes, glass bottles can be dumped overboard \n\n4) Yes, the bottles can be dumped if they are ground so that the resulting particles can pass through a screen with 25 mm openings",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Two reference points for pressure exist, absolute zero and atmospheric pressure. What are pressures measured relative to absolute zero called? \n\n1) Vacuum pressure \n\n2) Pressure drop \n\n3) Gauge pressure \n\n4) Absolute pressure",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)


        await add_question(test_id,
                           "Which of the following sensor type is preferred for detecting smoke from fire? \n\n1) Thermocouple \n\n2) Ionization type \n\n3) Thermometer \n\n4) Strain gauge",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Where should the placard you are shown be located, according to U.S. Coast Guard regulations? (Title 33-Navigation and Navigable waters, § 155.440) \n\n1) Both in a conspicuous place in each machinery space and in a conspicuous place at the bilge and ballast pump control station \n\n2) In the wheelhouse \n\n3) In a conspicuous place in each machinery space \n\n4) In a conspicuous place at the bilge and ballast pump control station",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Which of the following is not a methods of checking running motors for condition monitoring? \n\n1) Temperature of motor \n\n2) Measurement of insulation resistance \n\n3) Measurement of short circuit current \n\n4) Monitoring vibration due to defective bearings",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Ships of 10.000 tons gross tonnage and more, shall be fitted with oil filtering equipment, complying with Reg.14 (7) of MARPOL for the control of machinery space bilges. What would be the maximum oil content of oily-water mixture to pass through the filter? \n\n1) 60 ppm/n.m \n\n2) 100 ppm \n\n3) 30 ppm \n\n4) 15 ppm",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)


        await add_question(test_id,
                           "What type of protection is Ex e equipment? \n\n1) Increased safety \n\n2) Flameproof \n\n3) Non-sparking \n\n4) Pressurized",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Control triangular or ramp voltage (using Schmitt-trigger switching) can be produced by alternating charging and charging: \n\n1) An inductor with sinusoidal current \n\n2) A capacitor with a constant current \n\n3) A capacitor with sinusoidal current \n\n4) An inductor with constant current",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Where is OPA-90 applicable? \n\n1) Within US waters \n\n2) 200 nm off coast of California \n\n3) Within 200 nm of US waters including Guam, Hawaii, Alaska and San Juan \n\n4) 200 nm off US coast",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Which of the following is not an advantage of using a softstarter? \n\n1) It provides good soft starting and stopping with torque control \n\n2) It avoids nuisance tripping of generators when starting large motors \n\n3) It eliminates peak demand charges when starting large motors \n\n4) It eliminates occurrence of overvoltage during operation ",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)


        await add_question(test_id,
                           "Which electronic component or system is this graphical symbol illustrating: \n\n1) Bandpass filter \n\n2) 3-phase sine-wave generator \n\n3) Electric heater \n\n4) Transformer with ferromagnetic core",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "In US waters 'Oil Pollution Act of 1990' was activated in August 1993. What is the main issue for the introduction of the act? \n\n1) To enforce owners to use equipment of higher standards that those of today? \n\n2) To prevent oil spills in US waters? \n\n3) To encourage owners to build double hull vessels for trading US waters? \n\n4) To improve safety measures onboard?",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "When measuring level of liquids with a conductivity level indicator, measurement is performed by: \n\n1) Ionization chamber \n\n2) Capacitance probe \n\n3) Electrodes \n\n4) Displacement probe",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "When polarity of the incoming power line is reversed, what happens to the D.C. motor? \n\n1) Motor explodes \n\n2) Motor stalls \n\n3) Motor rotates in the reverse direction \n\n4) Motor still rotates in the same direction",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)


        await add_question(test_id,
                           "Use Kirchhoff's current law and Ohm's law to calculate the value of the current I for this circuit. \n\n1) 22A \n\n2) 72A \n\n3) 48A \n\n4) 2A",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The training manual shall contain instructions and information in easily understood terms and illustrated wherever possible. Which of the following objects have to be explained in detail in the manual according to present regulations? \n\n1) Donning of fire protection clothing \n\n2) Donning of lifejackets and immersion suits \n\n3) Starting of Main Engine \n\n4) Handling of stowaways",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Which of the following conditions could result in the exhaust from a diesel engine being dark coloured? \n\n1) Water in the fuel. \n\n2) Fuel injection pump timing too advanced. \n\n3) Some or all of the cylinders overloaded. \n\n4) Low charge air temperature.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "What does STCW deal with? \n\n1) STCW deals with training centre and schools and standards for watch keepers \n\n2) STCW deals with minimum recommendation for training centre and schools \n\n3) STCW deals with recommendation for training centre and schools and type of education for seafarers \n\n4) STCW deals with minimum recommendation of education for seafarers and minimum standards for training centre and schools",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)


        await add_question(test_id,
                           "Which of the following items must be included in each fire drill? \n\n1) All the items mentioned \n\n2) Reporting to stations and preparing for the duties described in the muster list \n\n3) Checking fireman's outfits and other personal rescue equipment \n\n4) Starting a fire pump using at least two required jets of water to show that the system is in proper working order",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "A triac is used to provide temperature control of an oven. The galley complain that the oven only reaches approximately 50% of the demanded temperature. Which of the following is a likely cause? \n\n1) Connection between the demand knob and the triac gate terminal has gone open circuit. \n\n2) One of the main switching elements in the triac has failed. \n\n3) The voltage supply to the oven controller is reduced by about 50% \n\n4) The triac has completely failed.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Who is responsible for the development of the Ship Security Plan? \n\n1) The Port Facility Security Officer \n\n2) The Ship Security Officer \n\n3) The Company Security Officer \n\n4) The Classification Society.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "A voltage measuring instrument has high impedance Zi. If the source impedance, Zg is much lower than Zi, what would be the relative measurement error? \n\n1) -Zg / (Zg + Zi) \n\n2) Zg / (Zg + Zi) \n\n3) Zg / Zi \n\n4) - Zg / Zi",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)


        await add_question(test_id,
                           "Who is responsible for the vessel's radio station and mandatory radio routines? \n\n1) The master. \n\n2) Statutory authorities. \n\n3) The radio officer. \n\n4) The owners.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The best way to ensure you get the equipment you need is to: \n\n1) Buy what everyone else is buying. \n\n2) Determine your needs and do some research. \n\n3) Buy the most expensive equipment on the market. \n\n4) Buy the newest models.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "When temperature of a gas is higher than normal temperature, what happens to the viscosity? \n\n1) Viscosity decreases \n\n2) Initial decrease before returning to original viscosity \n\n3) Viscosity increases \n\n4) No change in viscosity",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Diodes are widely used in rectification, or the conversion of alternating current to direct current. The sinusoidal input voltage V(in) is applied to the circuit shown. Which of the output voltages is correct? \n\n1) Figure 2 \n\n2) Figure 4 \n\n3) Figure 3 \n\n4) Figure 1",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)


        await add_question(test_id,
                           "Which one of the listed requirements regarding the stowage of lifeboats and life-rafts corresponds to present SOLAS regulations? \n\n1) Lifeboats shall be stowed attached to launching appliances. \n\n2) Life-rafts intended for throw-overboard launching shall be stowed midships secured to means for transfer to either side. \n\n3) Life-rafts shall be stowed close to the stern of the vessel \n\n4) Davit-launched life-rafts shall be stowed on starboard side of the ship.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "In control systems it is often necessary to convert from one type of unit to another. Which is a common signal level for an I/P converter? \n\n1) 0-20 mA/0-20 PSI \n\n2) 4-20mA/3-15 PSI \n\n3) 0-10V/3-15 PSI \n\n4) 0-1 mA/1-2 BAR",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "What is the function of automatic bus transfer (ABT) switch? \n\n1) It automatically connects the emergency generator to the emergency switchboard while disconnecting the main switchboard from the emergency switchboard \n\n2) It automatically connects the emergency generator to the main switchboard while disconnecting the main switchboard from the emergency switchboard \n\n3) It automatically connects the main generator to the main switchboard while disconnecting the main switchboard from the emergency switchboard \n\n4) It automatically connects the emergency generator to the main switchboard while disconnecting the main switchboard from the emergency switchboard",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "What is most important for crew members when preparing for emergencies? \n\n1) That people know where to find designated equipment \n\n2) That people know where to muster \n\n3) That people are well trained \n\n4) That people listen to orders given",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)


        await add_question(test_id,
                           "If drugs are discovered onboard your ship.... \n\n1) Notify the authorities after you arrive at the next port of call. \n\n2) Write a report a few days after the event and describe everything that occurred. \n\n3) Disembark crew and passengers as quickly as possible at the next port of call so the authorities can conduct their investigation. \n\n4) Ensure the witness to the discovery signs your incident report.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "When considering instrumentation systems, what is a typical symptom of a fault with the span of an instrument? \n\n1) Zero-point is accurate, but 100% input is not giving 100% output \n\n2) Linearity problems \n\n3) Zero-point and 100% are correct, but not at mid-range \n\n4) 100% output is accurate, but Zero-point is wrong",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Which of the following items shall be included in an \"abandon ship\"-drill? \n\n1) Checking that all crew and passenger moral is high \n\n2) Checking that passengers and crew are suitably dressed and lifejackets correctly donned \n\n3) Checking the distress signal rockets and other distress signals \n\n4) Checking the lifeboat provisions and supplies",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "What type of Ex equipment is suitable for installation in Zone 0 hazardous area? \n\n1) Ex d \n\n2) Ex m \n\n3) Ex i \n\n4) Ex p",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)


        await add_question(test_id,
                           "You are taking fuel on your vessel in the US when you notice oil on the water around your vessel. You are to stop taking fuel and: \n\n1) Leave the area. \n\n2) Notify the Corps of Engineers \n\n3) Begin clean up operations \n\n4) Notify the US Coast Guard",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "If you use chemicals for cleaning up an oil-spill on the water, what would the chemicals do? \n\n1) Disperse or dissolve the oil into the water \n\n2) Contain the oil within a small area \n\n3) Remove the oil from the water \n\n4) Absorb the oil for easy removal.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "\"Part way through a profiling interview with a supplier, the package the individual is carrying arouses your suspicion. What do you do?\" \n\n1) Call for help on the radio. \n\n2) Discreetly inform someone of your suspicions so he or she can get assistance. \n\n3) Confront the individual and demand that he open the package. \n\n4) Take the package and open it.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Which of the following is an application of an inductive sensor? \n\n1) Barometer \n\n2) Salinometer \n\n3) Tachometer \n\n4) Strain gauge",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)


        await add_question(test_id,
                           "Below shows a voltage-to-current converter. V+ = 10V, V- = -10V, Re = 5kΩ. When Vi = 0V, Ve = -0.6V. What is Ie? \n\n1) 2.25mA \n\n2) 0.127mA \n\n3) 4.25mA \n\n4) 1.88mA",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "\"A contractor is hired to install new navigation equipment onboard your ship while it's berthed. For a period of time he's left unsupervised and photographs schematics of the ship that he finds rolled up and stored in the corner of a nearby office. Later, from home, he hacks into the network and prints off information about the ship's security procedures. Which of these information security measures would have prevented his unauthorized access?\" \n\n1) \"Secure area, passwords, a firewall and a secure network.\" \n\n2) \"Firewall, protective markings, vetting and passwords.\" \n\n3) \"Protective markings, reference checks, and passwords.\" \n\n4) \"Secure area, passwords, a firewall and protective markings.\"",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "What type of valve is below picture showing? \n\n1) Plug valve \n\n2) Butterfly valve \n\n3) Ball valve \n\n4) Diaphragm valve",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "The Declaration of Security: \n\n1) Addresses the security requirements shared between ships or between a port facility and a ship. \n\n2) States the reporting procedures to government contact points. \n\n3) Identifies the security responsibilities of shipboard personnel. \n\n4) Details a ship's security measures.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "Which of the following classified equipment is not allowed to be installed in a Zone 1 hazardous area? \n\n1) Ex d \n\n2) Ex m \n\n3) Ex n \n\n4) Ex p",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Which one of the listed requirements regarding abandon ship drills corresponds to present SOLAS regulation? \n\n1) Each lifeboat shall be launched, and maneuvered in the water with its assigned crew at least once every three months during an abandon ship drill \n\n2) Drills shall be conducted when the ship is in a harbour \n\n3) On ships on short international voyages, each lifeboat shall be launched and maneuvered in the water at least every six months \n\n4) All lifeboats shall be lowered during drills",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "A hand flare must have a burning period of at least \n\n1) 30 Sec \n\n2) 10 Min \n\n3) 5 Min \n\n4) 1 Min",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "What is the advantage of pulse-width modulated (PWM) drive? \n\n1) Produces smooth torque, low output harmonic currents \n\n2) Does not cause any energy loss during switching \n\n3) Stabilized back e.m.f in the drive \n\n4) Stabilize fluctuations in voltage in the drive",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "Your vessel has been involved in a collision, which has resulted in a heavy oil leakage. Who should be called to handle pollution claims and damages? \n\n1) The Classification Society's representative. \n\n2) The P & I Club's nearest representative. \n\n3) The Leading Hull Underwriter's nearest Average Agent. \n\n4) Flag state representative.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Who is responsible that regulatory working hours are not exceeded? \n\n1) The individual person. \n\n2) The bosun and the second engineer. \n\n3) The master and department heads. \n\n4) The safety officer.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "The pressure inlet to a pressure gauge is varied from zero to full scale and back to zero again. The output (indicating pressure) versus true pressure is shown in the diagram. The non-coincidence (mis-match) of the loading and unloading curve is due to internal friction in the instrument. What do we call this phenomenon? \n\n1) Dead band \n\n2) Threshold \n\n3) Resolution \n\n4) Hysteresis",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "What principle of measurement are viscosity controllers usually based on? \n\n1) Measurement of differential pressure \n\n2) Measurement of flow \n\n3) Measurement of two different temperatures \n\n4) Measurement of temperature",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "In the diagram below we want to verify the resistance of the PT100 sensor fitted with compensation. What is the correct calculation? \n\n1) R(Pt100) = R1 + R2 \n\n2) R(Pt100) = R1 - R2\n\n3) R(Pt100) = R1 x R2 \n\n4) R(Pt100) = R1 : R2",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "The circuit symbol is a driver for a solenoid valve S. What is the purpose of the diode IN 4002 connected in parallel to the solenoid S? \n\n1) Allowing stored energy in solenoid to dissipate as freewheel current and therefore prevent damage to transistor from inductive switching voltage. \n\n2) Making voltage drop of approximate 0.5V between the operational amplifier and the transistor 2N5194 to assist transistor biasing. \n\n3) Open circuit for current flow between the operational amplifier and the transistor 2N5194 \n\n4) Blocking for +15V to the emitter of the transistor 2N5194 to stop it from overheating.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "What type of generation and distribution system is used for high voltage system? \n\n1) 3 phase, 3-wire insulated \n\n2) Single phase, 2-wire neutral earthed \n\n3) 3 phase, 3-wire neutral earthed \n\n4) 3 phase, 4-wire insulated",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Shipboard Emergency Drills must be carried out at least (OPA-90): \n\n1) Once a year \n\n2) Once a week \n\n3) Once every six months \n\n4) Once a month",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)


        await add_question(test_id,
                           "Which of the following is not a function of a control valve? \n\n1) Measure flow \n\n2) Regulate rate \n\n3) Divert flow \n\n4) Interrupt flow",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Where do you find minimum drill requirements? \n\n1) In manager's instructions \n\n2) In the SOLAS convention and its annex \n\n3) In classification society rules \n\n4) In owner's instruction",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Which of the following is not normally used as a main switchboard incoming circuit breaker? \n\n1) Oil circuit breaker (OCB) \n\n2) Vacuum circuit breaker (VCB) \n\n3) Miniature circuit breaker (MCB) \n\n4) Air circuit breaker (ACB)",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Which of these actions should you take if your ship is successfully boarded by armed pirates? \n\n1) Scream in fear and refuse to cooperate. \n\n2) Keep quiet and ignore any questions you're asked. \n\n3) Fight back. \n\n4) Assure your captors that you're not planning an attack to overthrow them.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)


        await add_question(test_id,
                           "The most effective way to combat the threat of drug smuggling is to? \n\n1) \"Combining routine, but irregular searches of the ship with spontaneous targeted searches.\" \n\n2) Organize crew into pairs and conduct weekly searches of the ship. \n\n3) Perform spontaneous targeted searches using teams of two or more personnel from the same department. \n\n4) \"Perform routine, but irregular searches using teams of two or more personnel from the same department.\"",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "What is the function of dynamic braking in fast moving motor? \n\n1) Stop the motor \n\n2) Slowing down the motor \n\n3) Protect the motor from getting damaged by friction brake \n\n4) Momentarily slows down a motor before speeding up when dynamic braking is released",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Your vessel has been involved in a collision, and at first opportunity a lot of people from outsides parties are asking questions. What shall you tell them? \n\n1) To make sure that all parties are informed about the facts, show them the extracts of the log-book. \n\n2) Do not tell anybody anything, except representatives from the main newspapers, radio and TV. Remember, the people have the right to know. \n\n3) Do not reply to any questions from outside parties, except the Solicitor appointed by your company. \n\n4) You shall only tell them the truth and nothing but the truth.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Which of the following would be considered pollution, when discharged overboard, under the US water pollution laws? \n\n1) Oil \n\n2) Garbage \n\n3) Hazardous substances \n\n4) All of the mentioned",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)


        await add_question(test_id,
                           "Thermo-elements will typically have \n\n1) Relatively wide range of temperature measurement \n\n2) A tendency to load the instrumentation system \n\n3) No influence at all on the readings \n\n4) Relatively narrow range of temperature measurement",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Eavesdropping and phone taps are examples of which threat to information security? \n\n1) Subversion \n\n2) Espionage \n\n3) Terrorism \n\n4) Sabotage",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "In relation to exhaust gas measurement with a thermocouple, use of an amplifier which gives a mA-signal out is preferred. Why is this done? \n\n1) The output signal from a thermocouple is at mV level, and cannot be transferred over any long distance without loss of signal, giving a poor accuracy and poor noise immunity. \n\n2) The signal out from the thermocouple is also mA, but have to be amplified in order to give a good signal to the alarm system. \n\n3) This depends on the length of the compensation-cable. \n\n4) To stabilize the signal and make it easier to measure at the receiver.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "One cylinder of a diesel engine is operating with a high exhaust gas temperature. From the options given, select the one most likely to cause this condition. \n\n1) Cylinder lubricating oil supply rate to the engine is excessive. \n\n2) The charge air is delivered to the engine at too high a temperature. \n\n3) Fuel injection valve opening pressure is too low. \n\n4) Water leakage into the cylinder.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)


        await add_question(test_id,
                           "Which function is this operational amplifier circuit performing? \n\n1) Non-inverting amplifier \n\n2) Inverting amplifier \n\n3) Integrator \n\n4) Differentiator",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Which alternative is correct for measuring current through the load L? \n\n1) Figure 3. \n\n2) Figure 4. \n\n3) Figure 2. \n\n4) Figure 1.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Which of the following is not an indication of a fully charged battery cell? \n\n1) Constant voltage of the cell with small tolerance \n\n2) Low density of electrolyte \n\n3) Deep chocolate brown for anode and clear slate-grey for cathode \n\n4) Gassing at the anode and cathode",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "What can lead to \"Unlimited responsibility\" (OPA-90)? \n\n1) Only wilful misconduct  \n\n2) Wilful misconduct and gross negligence \n\n3) Wilful misconduct, gross negligence and violation of Federal Safety \n\n4) Only gross negligence",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)


        await add_question(test_id,
                           "This circuit consists of a current source I, a change-over switch S, a resistor R and a capacitor C. The current/time figures 1 to 4 show possible changes in the current I when the switch S is suddenly shifted from position 1 to 2 at time t=0. Which diagram is correct? \n\n1) Figure A \n\n2) Figure B \n\n3) Figure C \n\n4) Figure D",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Which of these statements about drug smuggling is true? \n\n1) Drug smuggling is only a problem in certain ports, so only ships sailing in those ports need to implement preventative measures. \n\n2) The risks to ships are not restricted to specific areas or trading routes. \n\n3) Drugs are difficult to conceal onboard a ship. \n\n4) The preventative measures you incorporate into your ship's security plan should be exhaustive, regardless of the level of threat identified by your ship's security assessment.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "In a fresh water tank we are using a pressure transmitter with a range of 0-0.5 bar/4-20mA for level measurement. The transmitter is installed 30 centimeters from the bottom of the tank, and the tank is 5 meters high. What will the output from the transmitter be when the tank is empty? \n\n1) 5,2 mA \n\n2) 2 mA \n\n3) 4 mA \n\n4) 2,8 mA.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Which statement(s) is true of a gasoline spill? \n\n1) It is visible for a shorter time than a fuel oil spill \n\n2) It will sink more rapidly than crude oil \n\n3) It is not covered by the pollution law \n\n4) It does little harm to marine life",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "Zener barriers are sometimes used to supply power to electronic equipment in hazardous areas. Which statement is correct with regards to power supply for equipment supplied through Zener-barriers? \n\n1) The 0-volts line must never be grounded. \n\n2) The -24V must never be grounded. \n\n3) The +24V must always be grounded.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "When measuring viscosity with a restricted flow viscometer, the preferred sensing device is: \n\n1) Bourdon tube \n\n2) Rotating cylinder \n\n3) Capacitance probe \n\n4) Capillary tube",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "What IMO conventions take care of the human safety at sea? \n\n1) It is the STCW 78/95 that take care of the human safety at sea \n\n2) It is the MARPOL conventions that take care of the human safety at sea \n\n3) There isn't any conventions that take care of the human safety at sea \n\n4) It is the SOLAS conventions that take care of the human safety at sea",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Which type of profiling is used to obtain information about rival companies and their employees? \n\n1) Criminal \n\n2) Commercial \n\n3) General \n\n4) Industrial",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)


        await add_question(test_id,
                           "Is there any special area under MARPOL where it is forbidden to pump out any sludge or oil residues? \n\n1) There isn't any special area where it is forbidden to pump out any sludge or oil residues \n\n2) There are 3 special areas: the Baltic Sea, Mediterranean Sea, and Black Sea where it is forbidden to pump out any sludge or oil residues \n\n3) There are 4 special areas: the Baltic Sea, Mediterranean Sea, Red Sea and Black Sea where it is forbidden to pump out any sludge or oil residues",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "What type of level sensing are point sensing probes typically used for in a tank? \n\n1) Temperature level sensing \n\n2) Continuous level sensing \n\n3) Pressure level sensing \n\n4) High-high or low-low level sensing",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "In case of pollution in US waters, do you always have to notify the National Response Center (OPA-90)? \n\n1) No, not if the local US State Authority is correctly notified \n\n2) Yes, within three (3) days \n\n3) No, only the shipowner can notify NRC \n\n4) Yes, within thirty (30) minutes",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Which of the following detailed explanations should be mentioned in the Training Manual? \n\n1) How to use escape routes and other escape methods \n\n2) How to use surface to air visual signals to be used by survivors \n\n3) How to use navigational equipment for survival crafts \n\n4) How to recover survival craft and rescue boats including stowage and securing",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)


        await add_question(test_id,
                           "What is the minimum starting requirement of an emergency generator? \n\n1) 1 set of starting device with stored energy capable for at least 3 consecutive starts. \n\n2) 2 separate starting devices each with stored energy capable for at least 4 consecutive starts. \n\n3) 3 separate starting devices each with stored energy capable for at least 3 consecutive starts.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "When the cable length exceeds approx. 10 meters we normally have to, in case of a Pt 100, in some way compensate for the cable resistance. Do we also have to do this if we choose to use a T802 temperature sensor? \n\n1) Yes \n\n2) Depends on temperature to be measured. \n\n3) Not applicable \n\n4) No",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Which of these measures would you implement to prevent drugs from being smuggled onboard your ship while it's berthed? \n\n1) 'Search some of the packages, spares and stores received.' \n\n2) Eliminate fore and aft deck watch at night. \n\n3) Check a portion of the bags and packages brought onboard. \n\n4) Maintain restricted areas.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "In which of these circumstances can your ship request a DoS? \n\n1) Your ship has added a new port to its list of ports of call. \n\n2) There is a heightened security risk for your ship and a port facility. \n\n3) Your ship is operating at a lower security level than the ship or port it is interfacing with. \n\n4) Your ship is conducting activities with a port or ship that is not required to implement an approved security plan.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)


        await add_question(test_id,
                           "Which of the telecommunication equipment does not require 18 hours of emergency power during main power failure? \n\n1) LAN network system \n\n2) Magnetic compass \n\n3) Gyro compass \n\n4) Radar",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "What is the minimum test voltage of a 690V switchboard for insulation resistance? \n\n1) 220V \n\n2) 500V \n\n3) 1000V \n\n4) 440V",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "In an automatic temperature control system, operating with a PID controller, which of the following settings or parameter adjustments may result in system oscillation? \n\n1) Too short D-time \n\n2) Gain too low \n\n3) Gain too high \n\n4) Temperature change",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "The first step in completing an SSA is to: \n\n1) Identify the key shipboard operations, systems, areas and personnel that are critical to protect. \n\n2) List the existing security measures. \n\n3) Develop an onboard security survey checklist \n\n4) Create a list of potential motives for security incidents against your ship.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)


        await add_question(test_id,
                           "Notification logging procedures (OPA-90): \n\n1) Only initial reports to be logged \n\n2) Every report or message must be logged including time and date \n\n3) Only communication with USCG \n\n4) Only verbal reports for documentation",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "The OPA-90 notification requirement is: \n\n1) Notify only if you mean that own vessel might be tracked and charged \n\n2) Notify as soon as you have knowledge of a spill exceeding 10 gallons of oil \n\n3) Notify as soon as you have knowledge of any spill, or threat of a spill \n\n4) Notify only if you mean that own vessel might be responsible",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "What is the effect of high operating temperature on insulation resistance of equipment? \n\n1) Insulation resistance increases then drops \n\n2) No effect \n\n3) Insulation resistance increases \n\n4) Insulation resistance reduces",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "An important quantity which is useful in circuit analysis is known as conductance G (Siemens). Which of the formulas A to D expresses the conductance for this circuit? \n\n1) G = 1/R \n\n2) G = 2*R \n\n3) G = R * I \n\n4) G = I/R",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "The diagram shows a calibration curve for a pressure gauge. What is an alternative name for the slope of the characteristic? \n\n1) Repeatability \n\n2) Sensitivity \n\n3) Hysteresis \n\n4) Off-set",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "For a search to be effective it must be: \n\n1) Inclusive of all personnel. \n\n2) Conducted by personnel with limited knowledge of the ship's layout. \n\n3) Centrally controlled. \n\n4) Organized haphazardly.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "220V is applied to a transformer. The primary side has full turns while the secondary side has half the turns. There is a resistive load of 10 ohms. What is the primary side current? \n\n1) 2.75A \n\n2) 8A \n\n3) 22A \n\n4) 5.5A",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "What is the bias value used for in a controller? \n\n1) It is used to remove steady state error at a reference set point \n\n2) It is used to speed up control response in slow process, vice versa \n\n3) It is used to adjust a controller's proportional response to error \n\n4) It is used to remove all error accumulated over time",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "Which of the functions is this operational amplifier circuit performing? \n\n1) Non-inverting amplifier \n\n2) Integrator \n\n3) Inverting amplifier \n\n4) Differentiator",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "What is the priority for the ship's management team when fire breaks out? \n\n1) The ship's management team must organise the fire teams and then the teams have to rescue missing personnel \n\n2) The ship's management team and the crew must evacuate the ship \n\n3) The ship's management team must fight the fire and then call the fire teams \n\n4) The ship's management team must call the nearest fire brigade and police station",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Following shows the circuit diagram and amplitude transfer characteristics of a particular filter. What is the filter called? \n\n1) High pass filter \n\n2) Low pass filter \n\n3) Bandpass filter \n\n4) Notch filter",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Who is responsible for the regular security inspections of the ship? \n\n1) The Classification Society. \n\n2) The Company Security Officer \n\n3) The Port Facility Security Officer \n\n4) The Ship Security Officer",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)


        await add_question(test_id,
                           "What type of D.C. motor is below diagram showing? \n\n1) Shunt wound \n\n2) Compound-wound \n\n3) Separately-excited \n\n4) Series wound",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Which of the following methods may a diode may be tested by? \n\n1) Use a Digital Multi-Meter set to measure ohms in forward and reverse directions. \n\n2) Use a Digital Multi-Meter set to check forward voltage and reverse current blocking \n\n3) Use an insulation resistance tester (Megger) \n\n4) Connect to low ohms resistance tester.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "For what period of time is the protection and environment committee elected? \n\n1) 5 - 6 years. \n\n2) 3 - 4 years. \n\n3) 1 - 2 years. \n\n4) 8 years.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "What size is a kilobyte? \n\n1) 16 bytes \n\n2) 1000 bytes \n\n3) 10000 bytes \n\n4) 1024 bytes",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)


        await add_question(test_id,
                           "In terms of an automated control system, what is meant by the expression 'Slave Controller'? \n\n1) The secondary controller in a cascade control system \n\n2) Feed water controller \n\n3) The controller is always working hard \n\n4) The controller is following a pre-set control sequence",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "In a closed loop system, how is the controller output determined by? \n\n1) It is determined by the set point only \n\n2) It is determined by difference between the process variable and set point \n\n3) It is determined by the final output \n\n4) It is determined by the process variable and noise",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "When current-carrying conductor is moved in a magnetic field of a motor, as a by-product of motor torque, __ is produced. \n\n1) Over-voltage \n\n2) Excitation \n\n3) Back e.m.f. \n\n4) Forward e.m.f.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "Give the meaning of the following symbol \n\n1) Survival craft distress pyrotechnic signals \n\n2) Survival craft portable radio \n\n3) EPIRB \n\n4) Rocket parachute flare",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)


        await add_question(test_id,
                           "What is an earth fault? \n\n1) It is a break in the insulation, allowing the conductor to touch the hull. \n\n2) It is a trip in the MCB. \n\n3) It is a break in the conductor, not allowing current to pass through. \n\n4) It is a double break in insulation of two conductors of different potential, allowing a large current to pass through.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Records relating to breaches of security and changes in security level must be secured against unauthorized access and available for review by contracting governments. \n\n1) TRUE \n\n2) . \n\n3) FALSE \n\n4) .",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The charge air pressure supplied to a diesel engine, which is normally 2.0 bar, is reduced to 1.5 bar. What will be the likely effect on the engine operation? \n\n1) The turbochargers cooling water flow will increase. \n\n2) The performance of the engine will be reduced noticeably. \n\n3) The performance of the engine will be similar to normal conditions. \n\n4) The cylinder cooling water flow will increase.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "What is the effect of the I (integration) function of a PID controller? \n\n1) Quick control \n\n2) Easy to change set-point \n\n3) It will try to reduce the deviation between set-point and process value \n\n4) It will slow down the control system",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)


        await add_question(test_id,
                           "What is the advantage of a transmitter with a narrow measurement range? \n\n1) Lower purchase cost \n\n2) Do not need any calibration \n\n3) Easy installation \n\n4) Better linearity and increased accuracy",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "What are the functions of a flag state administration? \n\n1) They have responsibility for setting, monitoring and enforcing standards of safety and pollution prevention on vessels flying the countries flag \n\n2) They maintain a record of all ship and their crews, and produce statistics involving ships from their country. \n\n3) They have responsibility for ensuring that ships are correctly manned and that crews' terms and conditions of employment are met satisfactorily \n\n4) They have responsibility for ensuring that ships are properly registered",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "What is the advantage of proportional–integral–derivative (PID) Control over on-off control? \n\n1) PID Control has fewer control elements compared to on-off control \n\n2) PID Control has the ability to operate the process with smaller error, thus reducing wear and tear on final control elements \n\n3) PID Control has faster response time compared to on-off control \n\n4) PID Control has faster response time compared to on-off control",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Which of the connections you are shown, are the dedicated shore connection (MARPOL-connection) for discharging of sewage? \n\n1) 1 \n\n2) 2 \n\n3) 4 \n\n4) 3",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)


        await add_question(test_id,
                           "What is signal attenuation? \n\n1) Weakening of signal's control \n\n2) Reduction in signal's noise \n\n3) Reduction in signal's transmission distance \n\n4) Reduction in the signal's strength or amplitude",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "Which of the following prevention actions offers the guarantee of an efficient intervention in an emergency? \n\n1) All the listed answers \n\n2) Training of the crew \n\n3) Planning of the emergency \n\n4) The installation of protective measures",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "What type of piping line does below figure represent? \n\n1) Inert gas line \n\n2) Pneumatic air line \n\n3) Hydraulic line \n\n4) Electric heat tracing line",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "Which of the following information shall be specified by the muster list? \n\n1) The specific duties assigned to passengers that are in charge of a group of others \n\n2) The abandon ship signal consisting of two long blasts \n\n3) Action to be taken by crew and passengers \n\n4) The muster list has been prepared and approved by the administration before the ship proceeds to sea",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)


        await add_question(test_id,
                           "Which of the following is not part of control valve assembly? \n\n1) Actuator \n\n2) Valve body \n\n3) Positioner \n\n4) Sensor",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "The range of a transducer is 0-200 bar, and the output signal is 4-20 mA. What is the output signal when the process value is 100 bar? \n\n1) 12 mA \n\n2) 10 mA \n\n3) 24 mA \n\n4) 4 mA",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Give the meaning of the following symbol \n\n1) Rocket parachute flares \n\n2) Radar transponder \n\n3) EPIRB \n\n4) Survival craft distress pyrotechnic signals",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)

        await add_question(test_id,
                           "What type of D.C. motor is below diagram showing? \n\n1) Shunt wound \n\n2) Compound-wound \n\n3) Series wound \n\n4) Separately-excited",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)


        await add_question(test_id,
                           "Who are responsible for safe working conditions onboard? \n\n1) The individual person. \n\n2) The officer of the watch. \n\n3) The safety officer. \n\n4) Master, Chief Engineer & Chief Officer.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)

        await add_question(test_id,
                           "The purpose of profiling is to? \n\n1) Get beneath the outer shell of an individual to obtain a more complete picture. \n\n2) Identify different personality types. \n\n3) Make judgements about people based on their appearance. \n\n4) Categorize people based on their nationality and ethnicity.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Which of these statements about drug smugglers modes of operating is true? \n\n1) \"Drugs smuggled by an organized conspiracy are usually concealed in a primary ship system such as the engine room or in a tank, void or compartment.\" \n\n2) An organized conspiracy usually smuggles a small amount of drugs. \n\n3) Individual entrepreneurs usually smuggle large quantities of drugs. \n\n4) Drugs hidden by individual entrepreneurs are usually difficult to detect.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "A current measuring instrument has low impedance Zi. If the source impedance, Zg is much higher than Zi, what would be the relative measurement error? \n\n1) Zi / (Zi + Zg) \n\n2) -Zi / Zg \n\n3) Zi / Zg \n\n4) Zi / (Zi + Zg)",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 2)


        await add_question(test_id,
                           "What is 1 byte? \n\n1) 16 bits \n\n2) 1024 bits \n\n3) 8 bits \n\n4) 32 bits",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 3)

        await add_question(test_id,
                           "What is meant by dead ship condition? \n\n1) Condition under which the main propulsion plant, boilers and auxiliaries are not in operation due to absence of power \n\n2) Condition under which any services needed for normal operational and habitable conditions are not working due to absence of main power \n\n3) Condition under which services needed to provide minimum living conditions are not working. \n\n4) Condition under which ship as a whole is in working order and functioning normally.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "You are on a vessel 10 nautical miles off the coast of Algeria, in the Mediterranean Sea. Are you allowed to dump food waste overboard? \n\n1) No, food waste cannot be dumped overboard \n\n2) Yes, the food waste can be dumped if it is ground so that the resulting particles can pass through a screen with 25 mm openings \n\n3) Yes, the food waste can be dumped if it is ground so that the resulting particles can pass through a screen with 50 mm openings \n\n4) Yes, all kind of food waste can be dumped overboard",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "What is a salinometer? \n\n1) Device that determines air pressure \n\n2) Device that measures pressure of water \n\n3) Device that detects gases in the atmosphere \n\n4) Device that measures impurities of water",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 4)


        await add_question(test_id,
                           "What is a \"passenger\" according to SOLAS regulations? \n\n1) Every person other than the Captain and the members of the crew or other persons employed or engaged onboard the ship in the business of that ship. \n\n2) Everyone who travels with a passenger ship \n\n3) Any person paying their voyage regardless of ship type \n\n4) Any person holding a ticket and travelling with a passenger ship",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The DoS addresses the responsibility for the security of the water around the ship and the verification of increased threat levels. \n\n1) TRUE \n\n2) . \n\n3) FALSE \n\n4) .",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "On the basis of their conductivity, materials can be classified as isolators, semiconductors or conductors. Which of the following is considered a conductor? \n\n1) Copper \n\n2) Germanium \n\n3) Silicon \n\n4) Phosphor",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "When temperature of a liquid is higher than normal temperature, what happens to the viscosity? \n\n1) Viscosity decreases \n\n2) Viscosity increases \n\n3) Initial decrease before returning to original viscosity \n\n4) No change in viscosity",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "A motor is found to be overheated. A maintenance check was done and there was no overload. What is the remedy to resolve the overheating? \n\n1) Ventilation passages may be blocked and should be blown out with compressed air \n\n2) Replace with new rotor \n\n3) Replace with new cables of sufficient current carrying capacity \n\n4) Check state of brushes and slip rings.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Below figure shows an instrument loop. Which of the following shows the correct instrument flow? \n\n1) TT sends signal to both TR and PID. PID then sends processed signal to I/P. I/P generates a pneumatic signal to operate valve \n\n2) PID sends signal to I/P. I/P then generates a pneumatic signal to operate valve. Valve then sends signal to TT which then sends signal to both PID and TR \n\n3) I/P sends pneumatic signal to operate valve. Valve then sends signals to TT which then sends signal to both TR and PID. PID then operates I/P \n\n4) Valve sends signal to TT. TT then sends signals to both PID and TR. PID processes and then sends signal to I/P",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "What is SOPEP? \n\n1) A Shipboard Oil Pollution Emergency Plan \n\n2) A Seafarer's Offical Pension and Employment Payment scheme \n\n3) A Shipboard Oil Pollution Exemption Procedure \n\n4) A Ship-Owners Permitted Entry Plan",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Which type of temperature sensor is used in this temperature measuring system shown? \n\n1) Thermocouple sensor \n\n2) Thermistor sensor \n\n3) Platinum resistance sensor \n\n4) Quartz sensor",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "Which of the following equipment is responsible for reducing power factor of ship system? \n\n1) Induction motors \n\n2) Synchronous motor \n\n3) Electrical switchboard \n\n4) Synchronous motor",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "It is important to be clear about the performance capability of measuring instruments. How is the accuracy of an instrument expressed? \n\n1) In % of full scale and to least significant digit \n\n2) In % of range and to least significant digit \n\n3) In % of deviation and to least significant digit \n\n4) In % of gauge readings and to least significant digit",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Information about your ship's security arrangements and procedures is stored electronically. Which of these measures will help safeguard it from potential threats? \n\n1) Passwords \n\n2) Work history verification \n\n3) Protective markings \n\n4) Encoded email messages",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "In tanker operations, there will be some areas and zones where flammable or explosive vapour, gas, or dust may be expected. Such areas are classified as hazardous. What is meant by hazardous area Zone 1? \n\n1) Flammable mixture is not continuously present, but will be present during normal operations. \n\n2) Flammable mixture is not present at all times. \n\n3) Flammable mixture is continuously present or present for long periods. \n\n4) Flammable mixture would not normally be present or it would be present for a short period only.",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "What does the abbreviation STCW stand for? \n\n1) The International Convention on Standards of Training, Certification and Watchkeeping of Seafarers \n\n2) Seafarer's Training and Competence of Watchkeepers \n\n3) The International Convention of Ship's Trading, Chartering and Waybills \n\n4) The International Shipowners, Transport and Cargo Work Convention",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "What is the alcohol content in the blood permissible under US legislation before it is defined as intoxication? \n\n1) 0,04 % \n\n2) 0,01 % \n\n3) 0,1 % \n\n4) 0,07 %",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "What type of bomb search should you conduct to avoid panic when the credibility of the threat is in doubt and you don't want to disrupt ship business? \n\n1) Nominated officers search \n\n2) External search team \n\n3) Crew search \n\n4) Known hiding spot search",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "What is the disadvantage of using chemicals on an oil-spill on the water? \n\n1) The chemicals make it difficult to remove the oil from the water \n\n2) It is difficult to apply the chemicals if the oil drifts away from the ship's side \n\n3) It is difficult to apply chemicals if there is any wind \n\n4) The water gets a white colour, which makes it easy to detect the oil-spill",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "A valve which is already tuned with controller is found to be improperly calibrated. What is the rectification that needs to be taken in order for valve to function properly with controller? \n\n1) Recalibrate the valve and retune the control loop \n\n2) Use controller to recalibrate the valve \n\n3) Recalibrate the valve only \n\n4) Retune the controller only",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "What is the skin effect? \n\n1) Current concentrating at parts of a conductor where back e.m.f. is minimum, increasing resistance and thus losses \n\n2) Current that occurs in motors where there is relative motion between the armature of the motor and magnetic field from the motor's winding \n\n3) Chemical process in which a substance loses or gains electrons \n\n4) Reduction in governor's reference speed as fuel position increases",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Onboard training should be organised in such a way that: \n\n1) It is an integral part of the overall training plan and does not contravene with the rest hours of the crew \n\n2) It does not contravene with the rest hours of the crew and each crew member is trained individually \n\n3) Each crew member is trained individually \n\n4) none of the above",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The steps of the embarkation ladder used must be spaced apart by a distance of: \n\n1) Equally spaced and not less than 300 mm or more than 380 mm \n\n2) 300 mm \n\n3) equally spaced, not less than 200 mm or more than 280 mm \n\n4) 200 mm",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "What should you do with the ashes from your vessels incinerator if you have incinerated garbage containing plastics? \n\n1) MARPOL demands discharge to a shore facility, regardless of content \n\n2) Discharge at sea providing you are more than 25 miles offshore \n\n3) Discharge at sea providing you are more than 12 miles offshore \n\n4) Discharge at sea providing you are not in any river or estuary",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Which of the following best describes a feed-forward control system? \n\n1) Control of the process inlet side \n\n2) The process continually oscillates \n\n3) Easy to obtain a perfect control \n\n4) Mathematical calculation of the system response",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Why is it important to have good relationship between the crew on board a vessel? \n\n1) It leads to better work performance and positive atmosphere among the crew \n\n2) It encourages crew to extend their contract \n\n3) It will prevent accidents from happening \n\n4) Crew comes to know each others problems",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Which personnel must undergo familiarization training on board? \n\n1) Everyone \n\n2) Only catering staff \n\n3) Only the deck officers \n\n4) Only the ratings",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "What function is this circuit performing? \n\n1) Differentiating \n\n2) Telemetering \n\n3) Integrating \n\n4) Modulating",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "On an oil tanker outside a special area, what is the maximum instantaneous rate of discharge of oil content per nautical mile? \n\n1) 30 litres per nautical mile \n\n2) 20 litres per nautical mile \n\n3) 60 litres per nautical mile \n\n4) 40 litres per nautical mile",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "The circuit consists of two inductors, L(1) = 6 H and L(2) = 12 H, in series. Calculate the equivalent total inductance. \n\n1) L(S) = 18H \n\n2) L(S) = 1.5 H \n\n3) L(S) = 0.5 H \n\n4) L(S) = 4H",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "A nameplate for an equipment used in Hazardous Area has the following description: Ex d IIB T4 What does T4 stand for? \n\n1) Maximum surface temperature class of equipment \n\n2) Ignition temperature of equipment \n\n3) Gas group of equipment \n\n4) Equipment with non-sparking protection",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "Given a power system having values of apparent and reactive power at 500kVA and 300kVAR respectively, what is the power factor valued at? \n\n1) 0.8 \n\n2) 0.6 \n\n3) 1.6 \n\n4) 1.0",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "When moving into an Emission Control Area for Sulphur, which of these is most important? \n\n1) That low Sulphur fuel is actually being burned before entry into the ECA \n\n2) That the change-over to low Sulphur fuel is started before arrival in port \n\n3) That the change-over to low Sulphur fuel is complete before arrival in port \n\n4) That the change-over to low Sulphur fuel was started before entry into the ECA",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "This is a parallel L-C circuit with a curve showing frequency- impedance characteristics. Which of the formulae A to D gives the resonant frequency fo? \n\n1) fo = 1 / (2*Pi* sqrt (L*C)) \n\n2) fo = Pi*sqrt (L/C) / C \n\n3) fo = 1 / sqrt (1 - LC) \n\n4) fo = 1 / (Pi*sqrt (1 - LC))",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "Which of the following is not a mode of a closed loop control? \n\n1) Manual \n\n2) Modulation \n\n3) PID \n\n4) On-off",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)


        await add_question(test_id,
                           "What is the result of an 'unusually large metacentric height'? \n\n1) The vessel will roll violently \n\n2) The vessel will have a great bending moment \n\n3) The vessel will roll slowly or be unstable \n\n4) The vessel's tweendeck heights is too high",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "What is usually the effect on G when the ship is damaged below the waterline, with water ingress? \n\n1) It lowers \n\n2) It first rises then lowers \n\n3) It rises \n\n4) It is unchanged",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "From the list below, which is among the recommended actions for a vessel to take, on entering an area known for pirate activity? \n\n1) To transit with maximum safe speed \n\n2) To turn off all lights \n\n3) To confine all ship's personnel to one room onboard \n\n4) To transit at night time only",
                           "https://t.me/picturesforbo/105", [
                               "Answer 1",
                               "Answer 2",
                               "Answer 3",
                               "Answer 4"
                           ], 1)

        await add_question(test_id,
                           "As far as possible, all engines in lifeboats and rescue boats should be run \n\n1) for a total period of not less than 3 minutes every week \n\n2) for a total period of not less than 3 minutes every month \n\n3) for a total period of not less than 10 minutes every week \n\n4) for a total period of not less than 5 minutes every month",
                           "https://t.me/picturesforbo/105", [
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