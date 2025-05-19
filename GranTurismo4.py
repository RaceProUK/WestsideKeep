from __future__ import annotations

from typing import List, Set

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

@dataclass
class GT4APOptions:
    gran_turismo_4_include_arcade_mode: GT4IncludeArcadeMode
    gran_turismo_4_include_career_mode: GT4IncludeCareerMode
    gran_turismo_4_arcade_track_types: GT4ArcadeTrackTypes
    gran_turismo_4_career_sections: GT4CareerSections
    gran_turismo_4_driving_mission_types: GT4DrivingMissionTypes

class GT4IncludeArcadeMode(Toggle):
    """
    Allow Arcade Mode races as objectives
    """
    display_name = "Include Arcade Mode"

class GT4IncludeCareerMode(Toggle):
    """
    Allow Gran Turismo Mode races as objectives
    """
    display_name = "Include Gran Turismo Mode"

class GT4ArcadeTrackTypes(OptionSet):
    """
    Which track types are allowed for Arcade Mode objectives:
    - World Circuits
    - Original Circuits
    - City Courses
    - Dirt & Snow
    """
    display_name = "Arcade Mode Track Types"
    valid_keys = ["World Circuits", "Original Circuits", "City Courses", "Dirt & Snow"]
    default = valid_keys

class GT4CareerSections(OptionSet):
    """
    Which parts of Gran Turismo Mode are allowed for objectives:
    - Licenses
    - Beginner Events
    - Professional Events
    - Extreme Events
    - Endurance Events
    - Special Conditions
    - Regional Events
    - Manufacturer Events
    - Driving Missions
    """
    display_name = "Gran Turismo Mode Objective Areas"
    valid_keys = [
        "Licenses", "Beginner Events", "Professional Events", "Extreme Events", "Endurance Events",
        "Special Conditions", "Regional Events", "Manufacturer Events", "Driving Missions"
    ]
    default = valid_keys

class GT4DrivingMissionTypes(OptionSet):
    """
    Which types of driving missions are allowed for objectives:
    - The Pass
    - 3 Lap Battle
    - Slipstream Battle
    - 1 Lap Magic
    """
    display_name = "Driving Mission Types"
    valid_keys = ["The Pass", "3 Lap Battle", "Slipstream Battle", "1 Lap Magic"]
    default = valid_keys

class GranTurismo4(Game):
    name = "Gran Turismo 4"
    platform = KeymastersKeepGamePlatforms.PS2
    is_adult_only_or_unrated = False
    options_cls = GT4APOptions
    
    @property
    def include_arcade_mode(self) -> bool:
        return bool(self.archipelago_options.gran_turismo_4_include_arcade_mode.value)
    
    @property
    def include_career_mode(self) -> bool:
        return bool(self.archipelago_options.gran_turismo_4_include_career_mode.value)
    
    @property
    def arcade_track_types(self) -> Set[str]:
        return self.archipelago_options.gran_turismo_4_arcade_track_types.value
    
    @property
    def driving_mission_types(self) -> Set[str]:
        return self.archipelago_options.gran_turismo_4_driving_mission_types.value
    
    @property
    def career_sections(self) -> Set[str]:
        return self.archipelago_options.gran_turismo_4_dr.value
    
    @property
    def include_world_tracks(self) -> bool:
        return "World Circuits" in self.arcade_track_types
    
    @property
    def include_original_tracks(self) -> bool:
        return "Original Circuits" in self.arcade_track_types
    
    @property
    def include_city_tracks(self) -> bool:
        return "City Courses" in self.arcade_track_types
    
    @property
    def include_rally_tracks(self) -> bool:
        return "Dirt & Snow" in self.arcade_track_types
    
    @property
    def include_licence_tests(self) -> bool:
        return "Licenses" in self.career_sections
    
    @property
    def include_beginner_events(self) -> bool:
        return "Beginner Events" in self.career_sections
    
    @property
    def include_professional_events(self) -> bool:
        return "Professional Events" in self.career_sections
    
    @property
    def include_extreme_events(self) -> bool:
        return "Extreme Events" in self.career_sections
    
    @property
    def include_endurance_events(self) -> bool:
        return "Endurance Events" in self.career_sections
    
    @property
    def include_special_conditions(self) -> bool:
        return "Special Conditions" in self.career_sections
    
    @property
    def include_regional_events(self) -> bool:
        return "Regional Events" in self.career_sections
    
    @property
    def include_manufacturer_events(self) -> bool:
        return "Manufacturer Events" in self.career_sections
    
    @property
    def include_driving_missions(self) -> bool:
        return "Driving Missions" in self.career_sections
    
    @property
    def include_the_pass_missions(self) -> bool:
        return "The Pass" in self.driving_mission_types
    
    @property
    def include_3_lap_battle_missions(self) -> bool:
        return "3 Lap Battle" in self.driving_mission_types
    
    @property
    def include_slipstream_battle_missions(self) -> bool:
        return "Slipstream Battle" in self.driving_mission_types
    
    @property
    def include_1_lap_magic_missions(self) -> bool:
        return "1 Lap Magic" in self.driving_mission_types
    
    def arcade_world_tracks(self) -> List[str]:
        return [
            "Tsukuba Circuit (Dry)", "Tsukuba Circuit (Wet)",
            "Mazda Raceway Laguna Seca", "Nürburgring Nordschleife",
            "Infineon Raceway Sports Car Course", "Infineon Raceway Stock Car Course",
            "Twin Ring Motegi East Short Course", "Twin Ring Motegi West Short Course",
            "Twin Ring Motegi Road Course", "Twin Ring Motegi Super Speedway",
            "Suzuka Circuit East", "Suzuka Circuit West", "Suzuka Circuit",
            "Fuji Speedway '80s", "Fuji Speedway '90s",
            "Fuji Speedway 2005 GT", "Fuji Speedway 2005",
            "Circuit de la Sarthe I", "Circuit de la Sarthe II"
        ]
    
    def arcade_original_tracks(self) -> List[str]:
        return [
            "El Capitan", "High Speed Ring", "Trial Mountain Circuit", "Grand Valley East", "Grand Valley Speedway",
            "Autumn Ring", "Autumn Ring Mini", "Deep Forest Raceway", "Apricot Hill Raceway",
            "Mid-Field Raceway", "Beginner Course", "Motorland", "Test Course"
        ]
    
    def arcade_city_tracks(self) -> List[str]:
        return [
            "Clubman Stage Route 5", "Special Stage Route 5", "New York", "Seattle Circuit",
            "Tokyo R246", "Opera Paris", "Hong Kong", "Seoul Central", "Côte d'Azur"
        ]
    
    def arcade_city_duels(self) -> List[str]:
        return ["George V Paris", "Costa di Amalfi", "Citta di Aria"]
    
    def arcade_rally_tracks(self) -> List[str]:
        return [
            "Ice Arena", "Chamonix", "Grand Canyon", "Swiss Alps",
            "Tahiti Maze", "Cathedral Rocks Trail I", "Cathedral Rocks Trail II"
        ]
    
    def licence_tests(self) -> List[str]:
        return [f"{l}-{n}" for l in ["B", "A", "IB", "IA", "S"] for n in range(1, 16)]
    
    def beginner_events(self) -> List[str]:
        sets = {
            "Sunday Cup": 5,
            "FF Challenge": 5,
            "FR Challenge": 5,
            "4WD Challenge": 5,
            "MR Challenge": 5,
            "Light-weight K-Car Cup": 3,
            "Spider & Roadster": 3,
            "Sport Truck Race": 3
        }
        return [f"{series} Race {n + 1}" for series, count in sets.items() for n in range(0, count)]
    
    def professional_events(self) -> List[str]:
        sets = {
            "Clubman Cup": 5,
            "Tuning Car Grand Prix": 5,
            "Race of NA Sport": 5,
            "Race of Turbo Sport": 5,
            "Boxer Spirit": 3,
            "World Classics": 5,
            "Supercar Festival": 5,
            "Gran Turismo World Championship": 10
        }
        return [f"{series} Race {n + 1}" for series, count in sets.items() for n in range(0, count)]
    
    def extreme_events(self) -> List[str]:
        sets = {
            "Gran Turismo All Stars": 10,
            "Dream Car Championship": 10,
            "Polyphony Digital Cup": 10,
            "Like the Wind": 1,
            "Formula GT World Championship": 15,
            "World Circuit Tour": 8,
            "Premium Sports Lounge": 5
        }
        return [f"{series} Race {n + 1}" for series, count in sets.items() for n in range(0, count)]
    
    def endurance_events(self) -> List[str]:
        return [
            "Grand Valley 300km", "Laguna Seca 200 miles", "Roadster 4h",
            "Tokyo R246 300km", "Super Speedway 150 miles",
            "Nurburgring 24h", "Nurburgring 4h",
            "Suzuka 1000km", "Motegi 8h", "Tsukuba 9h",
            "Circuit de la Sarthe 24 h I", "Circuit de la Sarthe 24 h II",
            "Fuji 1000km", "Infineon World Sports",
            "El Capitan 200 miles", "New York 200 miles"
        ]
    
    def special_conditions(self) -> List[str]:
        sets = {
            "Capri Rally": 2,
            "Chamonix Rally": 2,
            "George V Rally": 2,
            "Grand Canyon Rally": 2,
            "Swiss Alps Rally": 2,
            "Tour of Tahiti": 2,
            "Tsukuba Wet Race": 1,
            "Umbria Rally": 2,
            "Whistler Ice Race": 2,
            "Yosemite Rally I": 2,
            "Yosemite Rally II": 2
        }
        return [f"{series} Race {n + 1}" for series, count in sets.items() for n in range(0, count)]
    
    def special_conditions_levels(self) -> List[str]:
        return ["Easy", "Normal", "Hard"]
    
    def regional_events(self) -> List[str]:
        return []
    
    def manufacturer_events(self) -> List[str]:
        return []
    
    def the_pass_missions(self) -> List[int]:
        return list(range(1, 10))
    
    def three_lap_battle_missions(self) -> List[int]:
        return list(range(11, 10))
    
    def slipstream_battle_missions(self) -> List[int]:
        return list(range(21, 4))
    
    def one_lap_magic_missions(self) -> List[int]:
        return list(range(25, 10))
    
    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return []
    
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return self.get_arcade_objectives() + self.get_career_objectives()
    
    def get_arcade_objectives(self) -> List[GameObjectiveTemplate]:
        return (self.get_world_tracks_objectives() +
                self.get_original_tracks_objectives() +
                self.get_city_tracks_objectives() +
                self.get_rally_tracks_objectives()
                if self.include_arcade_mode else [])
    
    def get_world_tracks_objectives(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label = "Stand on the podium at TRACK in Arcade Mode!",
                data = {
                    "TRACK": (self.arcade_world_tracks, 1)
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 3
            ),
            GameObjectiveTemplate(
                label = "Win the race at TRACK in Arcade Mode!",
                data = {
                    "TRACK": (self.arcade_world_tracks, 1)
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 3
            )
        ] if self.include_world_tracks else []
    
    def get_original_tracks_objectives(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label = "Stand on the podium at TRACK in Arcade Mode!",
                data = {
                    "TRACK": (self.arcade_original_tracks, 1)
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 3
            ),
            GameObjectiveTemplate(
                label = "Win the race at TRACK in Arcade Mode!",
                data = {
                    "TRACK": (self.arcade_original_tracks, 1)
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 3
            )
        ] if self.include_original_tracks else []
    
    def get_city_tracks_objectives(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label = "Stand on the podium at TRACK in Arcade Mode!",
                data = {
                    "TRACK": (self.arcade_city_tracks, 1)
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 3
            ),
            GameObjectiveTemplate(
                label = "Win the race at TRACK in Arcade Mode!",
                data = {
                    "TRACK": (self.arcade_city_tracks, 1)
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 3
            ),
            GameObjectiveTemplate(
                label = "Win the race at TRACK in Arcade Mode!",
                data = {
                    "TRACK": (self.arcade_city_duels, 1)
                },
                is_time_consuming = False,
                is_difficult = True,
                weight = 3
            )
        ] if self.include_city_tracks else []
    
    def get_rally_tracks_objectives(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label = "Win the race at TRACK in Arcade Mode!",
                data = {
                    "TRACK": (self.arcade_rally_tracks, 1)
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 3
            )
        ] if self.include_rally_tracks else []
    
    def get_career_objectives(self) -> List[GameObjectiveTemplate]:
        return (self.get_licence_objectives() +
                self.get_beginner_events_objectives() +
                self.get_professional_events_objectives() +
                self.get_extreme_events_objectives() +
                self.get_endurance_events_objectives() +
                self.get_special_conditions_objectives() +
                self.get_regional_events_objectives() +
                self.get_manufacturer_events_objectives() +
                self.get_driving_missions_objectives()
                if self.include_career_mode else [])
    
    def get_licence_objectives(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label = "Beat the target time in licence test LICENCE!",
                data = {
                    "LICENCE": (self.licence_tests, 1)
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 3
            ),
            GameObjectiveTemplate(
                label = "Get the Gold Medal in licence test LICENCE!",
                data = {
                    "LICENCE": (self.licence_tests, 1)
                },
                is_time_consuming = False,
                is_difficult = True,
                weight = 3
            )
        ] if self.include_licence_tests else []
    
    def get_beginner_events_objectives(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label = "Stand on the podium in the RACE!",
                data = {
                    "RACE": (self.beginner_events, 1)
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 3
            ),           
            GameObjectiveTemplate(
                label = "Win the RACE!",
                data = {
                    "RACE": (self.beginner_events, 1)
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 3
            )
        ] if self.include_beginner_events else []
    
    def get_professional_events_objectives(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label = "Stand on the podium in the RACE!",
                data = {
                    "RACE": (self.professional_events, 1)
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 3
            ),           
            GameObjectiveTemplate(
                label = "Win the RACE!",
                data = {
                    "RACE": (self.professional_events, 1)
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 3
            )
        ] if self.include_professional_events else []
    
    def get_extreme_events_objectives(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label = "Stand on the podium in the RACE!",
                data = {
                    "RACE": (self.extreme_events, 1)
                },
                is_time_consuming = True,
                is_difficult = True,
                weight = 3
            ),           
            GameObjectiveTemplate(
                label = "Win the RACE!",
                data = {
                    "RACE": (self.extreme_events, 1)
                },
                is_time_consuming = True,
                is_difficult = True,
                weight = 3
            )
        ] if self.include_extreme_events else []
    
    def get_endurance_events_objectives(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label = "Stand on the podium in the RACE!",
                data = {
                    "RACE": (self.endurance_events, 1)
                },
                is_time_consuming = True,
                is_difficult = False,
                weight = 3
            ),           
            GameObjectiveTemplate(
                label = "Win the RACE!",
                data = {
                    "RACE": (self.endurance_events, 1)
                },
                is_time_consuming = True,
                is_difficult = False,
                weight = 3
            )
        ] if self.include_endurance_events else []
    
    def get_special_conditions_objectives(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label = "Win the LEVEL RACE!",
                data = {
                    "RACE": (self.special_conditions, 1),
                    "LEVEL": (self.special_conditions_levels, 1)
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 3
            )
        ] if self.include_special_conditions else []
    
    def get_regional_events_objectives(self) -> List[GameObjectiveTemplate]:
        return [] if self.include_regional_events else []
    
    def get_manufacturer_events_objectives(self) -> List[GameObjectiveTemplate]:
        return [] if self.include_manufacturer_events else []
    
    def get_driving_missions_objectives(self) -> List[GameObjectiveTemplate]:
        return (self.get_the_pass_objectives() +
                self.get_3_lap_battle_objectives() +
                self.get_slipstream_battle_objectives() +
                self.get_1_lap_magic_objectives()
                if self.include_driving_missions else [])
    
    def get_the_pass_objectives(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label = "Beat Mission MISSION!",
                data = {
                    "MISSION": (self.the_pass_missions, 1)
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 3
            )
        ] if self.include_the_pass_missions else []
    
    def get_3_lap_battle_objectives(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label = "Beat Mission MISSION!",
                data = {
                    "MISSION": (self.three_lap_battle_missions, 1)
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 3
            )
        ] if self.include_3_lap_battle_missions else []
    
    def get_slipstream_battle_objectives(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label = "Beat Mission MISSION!",
                data = {
                    "MISSION": (self.slipstream_battle_missions, 1)
                },
                is_time_consuming = False,
                is_difficult = True,
                weight = 3
            )
        ] if self.include_slipstream_battle_missions else []
    
    def get_1_lap_magic_objectives(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label = "Beat Mission MISSION!",
                data = {
                    "MISSION": (self.one_lap_magic_missions, 1)
                },
                is_time_consuming = False,
                is_difficult = True,
                weight = 3
            )
        ] if self.include_1_lap_magic_missions else []