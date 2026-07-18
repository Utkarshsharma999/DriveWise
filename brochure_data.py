# DriveWise - Metadata Aware Automotive RAG Assistant
# Sample car brochure data (simulating real PDF brochure content)
# In a real scenario, these would be extracted from actual PDF brochures

brochures = {
    "Hyundai": {
        "Creta": {
            "overview": {
                "text": "The Hyundai Creta is a compact SUV designed for Indian roads. It comes with a bold front grille, sharp LED headlamps, and connected LED tail lamps. The Creta is available in multiple variants including E, EX, S, SX, and SX(O). It offers a premium driving experience with advanced technology and safety features. The Creta is one of the best-selling SUVs in India and is known for its reliability and comfort.",
                "page": 1
            },
            "engine_performance": {
                "text": "The Hyundai Creta is available with three engine options. The 1.5L naturally aspirated petrol engine produces 115 PS of power and 144 Nm of torque, paired with a 6-speed manual or IVT automatic transmission. The 1.5L diesel engine delivers 116 PS of power and 250 Nm of torque with a 6-speed manual or 6-speed automatic transmission. The 1.4L turbo petrol engine generates 140 PS and 242 Nm of torque, mated to a 7-speed DCT automatic. The turbo variant offers the best performance with 0-100 kmph in about 9.5 seconds.",
                "page": 2
            },
            "mileage_fuel": {
                "text": "The Hyundai Creta offers competitive fuel efficiency across all variants. The 1.5L petrol manual delivers 16.8 kmpl while the IVT automatic gives 16.5 kmpl. The 1.5L diesel manual offers an impressive 21.4 kmpl and the automatic variant returns 18.5 kmpl. The 1.4L turbo petrol with DCT delivers 16.6 kmpl. The fuel tank capacity is 50 litres for all variants. The diesel variant is recommended for users who drive more than 1500 km per month.",
                "page": 3
            },
            "safety": {
                "text": "The Hyundai Creta comes loaded with safety features. It has 6 airbags across all variants, ABS with EBD, Electronic Stability Control (ESC), Hill Assist Control (HAC), Vehicle Stability Management (VSM), rear parking sensors, and a reverse camera. The higher variants also get ADAS Level 2 features including Forward Collision Avoidance, Lane Keeping Assist, Smart Cruise Control, and Blind Spot Collision Warning. The Creta has received a 5-star safety rating from Global NCAP.",
                "page": 4
            },
            "dimensions": {
                "text": "The Hyundai Creta measures 4330 mm in length, 1790 mm in width, and 1635 mm in height. The wheelbase is 2610 mm which provides ample cabin space. The ground clearance is 190 mm which is suitable for Indian road conditions. The boot space is 433 litres which can accommodate two large suitcases easily. The kerb weight ranges from 1210 kg to 1380 kg depending on the variant.",
                "page": 5
            },
            "interior_comfort": {
                "text": "The Hyundai Creta interior features a 10.25-inch touchscreen infotainment system with wireless Android Auto and Apple CarPlay. It has a fully digital 10.25-inch instrument cluster, Bose premium 8-speaker sound system, ventilated front seats, powered driver seat, panoramic sunroof, air purifier with AQI display, rear AC vents, wireless phone charger, and ambient lighting. The seats are wrapped in leather and the cabin uses premium soft-touch materials. The second row gets adjustable headrests and a center armrest with cup holders.",
                "page": 6
            },
            "infotainment": {
                "text": "The Hyundai Creta infotainment system includes a 10.25-inch HD touchscreen with navigation, Bluelink connected car technology with over 60 features including remote engine start, remote AC control, vehicle tracking, SOS emergency call, and geo-fence alert. It supports wireless Android Auto and Apple CarPlay, has voice recognition, and comes with 8 speakers by Bose. The system also supports OTA map updates and Alexa and Google Home integration for smart home connectivity.",
                "page": 7
            },
            "price_variants": {
                "text": "The Hyundai Creta price starts from Rs 11.0 lakh for the base E petrol variant and goes up to Rs 20.15 lakh for the top SX(O) turbo DCT variant (ex-showroom). The diesel variants range from Rs 12.5 lakh to Rs 19.99 lakh. The most popular variant is the SX variant which offers the best value for money with most features included. All prices are ex-showroom and may vary by city.",
                "page": 8
            }
        },
        "Venue": {
            "overview": {
                "text": "The Hyundai Venue is a sub-compact SUV designed for urban city driving. It features a sporty and youthful design with a cascading front grille, LED projector headlamps, and dual-tone roof options. The Venue is compact enough for easy city maneuvering while offering SUV-like presence on the road. It is available in E, S, SX, and SX(O) variants.",
                "page": 1
            },
            "engine_performance": {
                "text": "The Hyundai Venue comes with two engine options. The 1.2L Kappa petrol engine produces 83 PS and 114 Nm of torque paired with a 5-speed manual transmission. The 1.0L turbo GDi petrol engine delivers 120 PS and 172 Nm of torque mated to a 7-speed DCT automatic or 6-speed iMT (clutchless manual) transmission. The turbo variant is the better choice for highway driving and overtaking.",
                "page": 2
            },
            "mileage_fuel": {
                "text": "The Hyundai Venue fuel efficiency varies by engine. The 1.2L petrol manual delivers 17.5 kmpl. The 1.0L turbo with iMT gives 18.1 kmpl while the turbo DCT automatic returns 17.2 kmpl. The fuel tank capacity is 45 litres. For city driving, the Venue turbo iMT is the best option combining performance with efficiency.",
                "page": 3
            },
            "safety": {
                "text": "The Hyundai Venue safety features include 6 airbags, ABS with EBD, rear parking sensors with camera, Hill Assist Control, Electronic Stability Control, and ISOFIX child seat mounts. The higher variants also get TPMS (Tyre Pressure Monitoring System) and Highline TPMS. The Venue provides good all-round safety for a car in its segment.",
                "page": 4
            },
            "dimensions": {
                "text": "The Hyundai Venue is 3995 mm long, 1770 mm wide, and 1617 mm tall. The wheelbase is 2500 mm and the ground clearance is 195 mm. The boot space is 350 litres. The compact dimensions make it easy to park and navigate through tight city streets. The turning radius is 5.2 metres.",
                "page": 5
            },
            "interior_comfort": {
                "text": "The Hyundai Venue interior has an 8-inch touchscreen infotainment system with wireless Android Auto and Apple CarPlay. It features a digital instrument cluster, wireless phone charger, sunroof, rear AC vents, height-adjustable driver seat, and push-button start. The seats are fabric or leather depending on the variant. The cabin is well-designed with a driver-centric layout.",
                "page": 6
            },
            "price_variants": {
                "text": "The Hyundai Venue starts from Rs 7.94 lakh for the base E variant and goes up to Rs 13.48 lakh for the top SX(O) turbo DCT variant (ex-showroom). The best value variant is the S turbo iMT at around Rs 10.5 lakh which gives you the turbo engine with most essential features. All prices are ex-showroom.",
                "page": 7
            }
        },
        "i20": {
            "overview": {
                "text": "The Hyundai i20 is a premium hatchback that combines sporty design with practical everyday usability. It features Hyundai's Sensuous Sportiness design language with a wide cascading grille, Z-shaped LED tail lamps, and a low-slung stance. The i20 competes with the Maruti Baleno and Tata Altroz in the premium hatchback segment. It is available in Magna, Sportz, Asta, and Asta(O) variants.",
                "page": 1
            },
            "engine_performance": {
                "text": "The Hyundai i20 is available with three engine options. The 1.2L Kappa petrol engine produces 88 PS and 115 Nm paired with a 5-speed manual or CVT automatic. The 1.0L turbo GDi petrol delivers 120 PS and 172 Nm with 7-speed DCT or 6-speed iMT. The 1.5L diesel engine produces 100 PS and 240 Nm with a 6-speed manual. The turbo N Line variant gets sportier tuning.",
                "page": 2
            },
            "mileage_fuel": {
                "text": "The Hyundai i20 fuel efficiency is segment-leading. The 1.2L petrol manual gives 20.35 kmpl and the CVT gives 19.65 kmpl. The 1.0L turbo iMT delivers 20.25 kmpl and the DCT returns 19.10 kmpl. The 1.5L diesel manual delivers 25.2 kmpl making it the most fuel-efficient option. The fuel tank is 37 litres.",
                "page": 3
            },
            "safety": {
                "text": "The Hyundai i20 comes with 6 airbags, ABS with EBD, ESC, VSM, Hill Assist Control, rear parking sensors, reverse camera, and ISOFIX mounts. The top variants add TPMS and Highline TPMS. The i20 has scored well in safety assessments and provides a safe cabin for a hatchback.",
                "page": 4
            },
            "dimensions": {
                "text": "The Hyundai i20 is 3995 mm long, 1775 mm wide, and 1505 mm tall. The wheelbase is 2580 mm providing good rear legroom for a hatchback. Ground clearance is 170 mm. Boot space is 311 litres. The i20 feels wider and more planted than most hatchbacks thanks to its wide track.",
                "page": 5
            },
            "interior_comfort": {
                "text": "The Hyundai i20 cabin features a 10.25-inch touchscreen with Bluelink connected car tech, wireless Android Auto and Apple CarPlay, Bose 7-speaker system, sunroof, wireless charger, ambient lighting, air purifier, digital instrument cluster, and cruise control. The seats are comfortable with good cushioning for long drives. The rear seat has enough space for two adults comfortably.",
                "page": 6
            },
            "price_variants": {
                "text": "The Hyundai i20 price starts from Rs 7.04 lakh for the Magna 1.2 petrol and goes up to Rs 11.49 lakh for the Asta(O) turbo DCT variant. The diesel range is from Rs 8.64 lakh to Rs 10.70 lakh. The i20 N Line starts from Rs 10.09 lakh. The Sportz variant at around Rs 8.5 lakh is the sweet spot for most buyers.",
                "page": 7
            }
        }
    },
    "Tata": {
        "Nexon": {
            "overview": {
                "text": "The Tata Nexon is a sub-compact SUV and one of India's highest-selling SUVs. It was the first car in India to receive a 5-star Global NCAP safety rating. The Nexon features Tata's Impact 2.0 design language with a split headlamp setup, coupe-like roofline, and muscular body cladding. It is available in Smart, Pure, Creative, and Fearless variants.",
                "page": 1
            },
            "engine_performance": {
                "text": "The Tata Nexon comes with two engine options. The 1.2L turbocharged Revotron petrol engine produces 120 PS and 170 Nm of torque. The 1.5L turbocharged Revotorq diesel engine delivers 116 PS and 260 Nm of torque. Both engines are available with a 6-speed manual or 6-speed AMT automatic transmission. The diesel engine offers strong mid-range torque making it great for highway cruising.",
                "page": 2
            },
            "mileage_fuel": {
                "text": "The Tata Nexon petrol manual delivers 17.4 kmpl while the AMT gives 17.2 kmpl. The diesel manual offers 23.2 kmpl and the diesel AMT gives 22.1 kmpl. The fuel tank is 44 litres. The Nexon diesel is one of the most fuel-efficient SUVs in its segment, making it a good choice for high mileage users.",
                "page": 3
            },
            "safety": {
                "text": "The Tata Nexon has a 5-star Global NCAP safety rating. It comes with 6 airbags across all variants, ABS with EBD, Corner Stability Control, Electronic Stability Program, Hill Hold Control, ISOFIX child seat mounts, all four disc brakes, rear parking sensors with camera, and Tata's ESP with rollover mitigation. The Nexon's build quality and structural integrity are among the best in segment.",
                "page": 4
            },
            "dimensions": {
                "text": "The Tata Nexon measures 3994 mm in length, 1811 mm in width, and 1607 mm in height. The wheelbase is 2498 mm and ground clearance is 209 mm which is the best in segment. Boot space is 350 litres. The high ground clearance makes it capable on rough roads and speed breakers.",
                "page": 5
            },
            "interior_comfort": {
                "text": "The Tata Nexon interior has a 10.25-inch floating touchscreen with wireless Android Auto and Apple CarPlay, a 10.25-inch digital instrument cluster, automatic AC, ventilated leatherette seats, powered sunroof, air purifier, wireless phone charger, rain-sensing wipers, auto headlamps, and a 9-speaker Harman sound system. The seats offer good support and the cabin feels spacious for a sub-compact SUV.",
                "page": 6
            },
            "price_variants": {
                "text": "The Tata Nexon price starts from Rs 8.10 lakh for the Smart petrol variant and goes up to Rs 15.50 lakh for the top Fearless Plus diesel AMT variant (ex-showroom). The most popular variant is Creative Plus at around Rs 12.0 lakh which offers most features at a reasonable price. The Nexon offers strong value for money compared to competitors.",
                "page": 7
            }
        },
        "Harrier": {
            "overview": {
                "text": "The Tata Harrier is a mid-size SUV built on the OMEGA ARC platform derived from Land Rover's D8 architecture. It has a commanding road presence with its bold design, LED projector headlamps, and a wide muscular stance. The Harrier competes with the Hyundai Creta and Kia Seltos in the premium SUV segment. Available in Smart, Pure, Adventure, Fearless, and Accomplished variants.",
                "page": 1
            },
            "engine_performance": {
                "text": "The Tata Harrier is powered by a 2.0L Kryotec turbocharged diesel engine producing 170 PS of power and 350 Nm of torque. It is available with a 6-speed manual or 6-speed torque converter automatic transmission. The engine is refined and offers strong performance for highway driving. The automatic variant features Sport and Eco driving modes for different driving preferences.",
                "page": 2
            },
            "mileage_fuel": {
                "text": "The Tata Harrier diesel manual delivers 16.35 kmpl while the automatic variant returns 14.6 kmpl. The fuel tank capacity is 50 litres providing a good range on a full tank. For a car of its size and engine capacity, the Harrier offers reasonable fuel efficiency. Highway mileage is typically better at around 18-19 kmpl for the manual.",
                "page": 3
            },
            "safety": {
                "text": "The Tata Harrier comes with 6 airbags, ABS with EBD, Electronic Stability Program, Hill Hold and Hill Descent Control, all four disc brakes, ISOFIX child seat anchors, rear parking sensors with camera, Blind Spot Monitor, and ADAS features including Adaptive Cruise Control, Lane Departure Warning, and Autonomous Emergency Braking. The Harrier has a 5-star Global NCAP rating.",
                "page": 4
            },
            "dimensions": {
                "text": "The Tata Harrier is 4598 mm long, 1894 mm wide, and 1706 mm tall. The wheelbase is 2741 mm offering excellent rear legroom. Ground clearance is 205 mm and boot space is 425 litres. The Harrier is larger than most competitors in its price range giving it a premium feel and spacious cabin.",
                "page": 5
            },
            "interior_comfort": {
                "text": "The Tata Harrier cabin features a 12.3-inch floating touchscreen, 10.25-inch digital instrument cluster, panoramic sunroof, ventilated and powered front seats, 10-speaker JBL sound system, wireless charging, 4-zone automatic climate control, ambient lighting, powered tailgate, and premium leatherette upholstery. The cabin is quiet and well-insulated from road noise.",
                "page": 6
            },
            "price_variants": {
                "text": "The Tata Harrier starts from Rs 15.49 lakh for the Smart manual variant and goes up to Rs 26.44 lakh for the top Accomplished Plus automatic variant (ex-showroom). The Adventure Plus variant at around Rs 20 lakh is considered the best value variant. The Harrier offers Land Rover derived platform quality at an affordable price.",
                "page": 7
            }
        }
    },
    "Maruti Suzuki": {
        "Brezza": {
            "overview": {
                "text": "The Maruti Suzuki Brezza is a sub-compact SUV known for its reliability, low maintenance costs, and strong resale value. It features a bold neo-modern design with LED projector headlamps, a chrome-accented grille, and sporty dual-tone exterior options. The Brezza is one of the most popular SUVs in India backed by Maruti's extensive service network. Available in LXi, VXi, ZXi, and ZXi+ variants.",
                "page": 1
            },
            "engine_performance": {
                "text": "The Maruti Brezza is powered by a 1.5L K15C Dual Jet Dual VVT petrol engine with Smart Hybrid technology producing 103 PS and 137 Nm of torque. It is available with a 5-speed manual or 6-speed torque converter automatic transmission. The mild hybrid system provides torque assist during acceleration and improves fuel efficiency. The engine is smooth and refined for city driving.",
                "page": 2
            },
            "mileage_fuel": {
                "text": "The Maruti Brezza manual delivers 20.15 kmpl while the automatic gives 19.80 kmpl. With the Smart Hybrid technology the efficiency is among the best in segment. The fuel tank capacity is 48 litres. The Brezza is recommended for buyers who prioritize low running costs. CNG variant is also available delivering 25.0 km/kg.",
                "page": 3
            },
            "safety": {
                "text": "The Maruti Brezza comes with 6 airbags, ABS with EBD, ESP with Hill Hold Assist, rear parking sensors with camera, ISOFIX child seat mounts, and high-speed alert system. The top variants also get a 360-degree camera and head-up display. Maruti has significantly improved safety across its lineup in recent years.",
                "page": 4
            },
            "dimensions": {
                "text": "The Maruti Brezza measures 3995 mm in length, 1790 mm in width, and 1640 mm in height. The wheelbase is 2500 mm and ground clearance is 198 mm. Boot space is 328 litres. The compact size with good ground clearance makes it versatile for both city and rural roads.",
                "page": 5
            },
            "interior_comfort": {
                "text": "The Maruti Brezza interior features a 9-inch SmartPlay Pro+ touchscreen with wireless Android Auto and Apple CarPlay, a head-up display, 360-degree camera, sunroof, automatic AC with rear vents, cruise control, wireless charger, Arkamys-tuned 6-speaker system, and push-button start. The cabin layout is functional and practical with good storage spaces.",
                "page": 6
            },
            "price_variants": {
                "text": "The Maruti Brezza starts from Rs 8.34 lakh for the LXi manual and goes up to Rs 14.14 lakh for the ZXi+ automatic variant (ex-showroom). The ZXi variant at around Rs 11.5 lakh is the best value variant with most features. Maruti's service costs are among the lowest in the industry.",
                "page": 7
            }
        }
    }
}
