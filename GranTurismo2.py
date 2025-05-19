from __future__ import annotations

from typing import List, Set

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

@dataclass
class GT2APOptions:
    gran_turismo_2_include_arcade_mode: GT2IncludeArcadeMode
    gran_turismo_2_include_career_mode: GT2IncludeCareerMode
    gran_turismo_2_career_sections: GT2CareerSections

class GT2IncludeArcadeMode(Toggle):
    """
    Allow Arcade Mode races as objectives
    """
    display_name = "Include Arcade Mode"

class GT2IncludeCareerMode(Toggle):
    """
    Allow Gran Turismo Mode races as objectives
    """
    display_name = "Include Gran Turismo Mode"

class GT2CareerSections(OptionSet):
    """
    Which parts of Gran Turismo Mode are allowed for objectives:
    - Licenses
    - Gran Turismo League
    - Special Events
    - Dirt Events
    - Manufacturer Events
    - Event Generator (also known as the Event Synthesizer)
    - Endurance
    """
    display_name = "Gran Turismo Mode Objective Areas"
    valid_keys = ["Licenses", "Gran Turismo League", "Special Events", "Dirt Events", "Manufacturer Events", "Event Generator", "Endurance"]
    default = valid_keys

class GranTurismo2(Game):
    name = "Gran Turismo 2"
    platform = KeymastersKeepGamePlatforms.PS1
    is_adult_only_or_unrated = False
    options_cls = GT2APOptions
    
    @property
    def include_arcade_mode(self) -> bool:
        return bool(self.archipelago_options.gran_turismo_2_include_arcade_mode.value)
    
    @property
    def include_career_mode(self) -> bool:
        return bool(self.archipelago_options.gran_turismo_2_include_career_mode.value)
    
    @property
    def career_sections(self) -> Set[str]:
        return self.archipelago_options.gran_turismo_2_career_sections.value
    
    @property
    def include_licence_tests(self) -> bool:
        return "Licenses" in self.career_sections
    
    @property
    def include_gt_league(self) -> bool:
        return "Gran Turismo League" in self.career_sections
    
    @property
    def include_special_events(self) -> bool:
        return "Special Events" in self.career_sections
    
    @property
    def include_rally_events(self) -> bool:
        return "Dirt Events" in self.career_sections
    
    @property
    def include_maker_events(self) -> bool:
        return "Manufacturer Events" in self.career_sections
    
    @property
    def include_event_synth(self) -> bool:
        return "Event Generator" in self.career_sections
    
    @property
    def include_endurances(self) -> bool:
        return "Endurance" in self.career_sections
    
    def arcade_classes(self) -> List[str]:
        return ["C", "B", "A", "S"]
    
    def arcade_ranks(self) -> List[str]:
        return ["Easy", "Normal"]
    
    def arcade_hard_ranks(self) -> List[str]:
        return ["Difficult"]
    
    def arcade_tarmac_tracks(self) -> List[str]:
        return [
            "Tahiti Road", "Midfield Raceway", "High Speed Ring",
            "Super Speedway", "Seattle Short Course", "Rome Short Course",
            "Red Rock Valley Speedway", "Seattle Circuit", "Rome Circuit",
            "Grindelwald", "Laguna Seca Raceway", "Apricot Hill Speedway",
            "Trial Mountain Circuit", "Clubman Stage Route 5", "Grand Valley East Section",
            "Grand Valley Speedway", "Special Stage Route 5", "Autumn Ring",
            "Test Course", "Deep Forest Raceway", "Rome Night"
        ]
    
    def licence_tests(self) -> List[str]:
        return [f"{l}-{n}" for l in ["B", "A", "IC", "IB", "IA", "S"] for n in range(1, 10)]
    
    def gt_league_races(self) -> List[str]:
        sets = {
            "French Nationals": 2,
            "German Nationals": 3,
            "Italian Nationals": 2,
            "Japan Nationals": 3,
            "UK Nationals": 3,
            "US Nationals": 3,
            "Euro League": 3,
            "Pacific League": 3
        }
        return [f"{series} Race {n + 1}" for series, count in sets.items() for n in range(0, count)]
    
    def gt_league_series(self) -> List[str]:
        return ["World League"]
    
    def special_events_races(self) -> List[str]:
        sets = {
            "Sunday Cup": 3,
            "Clubman Cup": 3,
            "FF Challenge": 3,
            "FR Challenge": 3,
            "Mid-engine Challenge": 3,
            "4WD Challenge": 3,
            "Lightweight \"K\" Cup": 3,
            "Compact Car World Cup": 3,
            "Luxury Sedan Cup": 3,
            "Muscle Car Cup": 3,
            "Convertible Car World Cup": 3,
            "Historic Car Cup": 3,
            "Station Wagon Cup": 3,
            "80's Sports Car Cup": 5,
            "Grand Touring Car Trophy": 3,
            "Pure Sports Car Cup": 3,
            "Tuned NA Car No.1 Cup": 3,
            "Tuned Turbo Car No.1 Cup": 3,
            "Gran Turismo All-Stars": 5,
            "Super Touring Trophy": 5
        }
        return [f"{series} Race {n + 1}" for series, count in sets.items() for n in range(0, count)]
    
    def special_events_series(self) -> List[str]:
        return ["GT300 Championship", "GT500 Championship"]
    
    def dirt_events_races(self) -> List[str]:
        courses = [
            "Smokey Mountain South",
            "Smokey Mountain North",
            "Green Forest Roadway",
            "Tahiti Maze",
            "Tahiti Dirt Route 3",
            "Smokey Mountain North Reverse",
            "Tahiti Dirt Route 3 Reverse"
        ]
        return [f"{course} Race {n + 1}" for course in courses for n in range(0, 3)]
    
    def dirt_events_hard_races(self) -> List[str]:
        courses = [
            "Pikes Peak Downhill",
            "Pikes Peak Hill Climb"
        ]
        return [f"{course} Race {n + 1}" for course in courses for n in range(0, 3)]
    
    def maker_events_races(self) -> List[str]:
        return [
            "106 Challenge", "155 & 156 Race", "500 Meeting", "Altezza Cup", "Alto Works Cup",
            "Cappuccino Cup", "Celica Meeting", "Challenge S2000", "Civic Race", "Clio Cup",
            "Corvette Meeting", "Cuore Challenge", "DB-7 Trophy", "Delta Cup", "Demio Race",
            "Elan Trophy", "Elise Trophy", "Golf Cup", "GT-R Meeting",  "Ka Challenge",
            "March Trophy", "MGF Challenge", "Mini Challenge", "Mirage Cup", "MX-5 Trophy",
            "Neon Trophy", "New Beetle Challenge", "Saxo Challenge", "Silvia & 180SX Club",
            "Sirion Challenge", "SLK Trophy", "SVX Challenge", "Tigra Cup", "TT Challenge",
            "Tuscan Speed Challenge", "Viper Festival of Speed", "Yaris Trophy", "ZZ Challenge"
        ]
    
    def maker_events_styles(self) -> List[str]:
        return ["Normal", "Racing"]
    
    def maker_events_normal_only(self) -> List[str]:
        return [
            "3 Series Cup", "AZ-1 Challenge", "Beat the Beat", "Evolution Meeting", "Focus Challenge",
            "Impreza Challenge", "Midget Contest", "MR-S Trophy", "NSX Trophy", "Pulsar Cup",
            "RX-7 Meeting", "Skyline R34 Challenge", "Starlet Meeting", "Type R Meeting"
        ]
    
    def event_synth_ranks(self) -> List[str]:
        return ["Easy/Beginner", "Normal/Intermediate"]
    
    def event_synth_hard_ranks(self) -> List[str]:
        return ["Hard/Advanced"]
    
    def event_synth_long_ranks(self) -> List[str]:
        return ["Expert/Pro"]
    
    def endurances(self) -> List[str]:
        return [
            "Grand Valley 300km",
            "Apricot Hill 200km",
            "Seattle 100 Miles",
            "Laguna Seca 200 Miles",
            "Millennium Rome 2 Hours",
            "Trial Mountain 30 Laps",
            "Special Stage Route 5 All-Night"
        ]
    
    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return []
    
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return self.get_arcade_objectives() + self.get_career_objectives()
    
    def get_arcade_objectives(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label = "Stand on the podium at TRACK in Class CLASS at RANK level or higher in Arcade Mode!",
                data = {
                    "CLASS": (self.arcade_classes, 1),
                    "RANK": (self.arcade_ranks, 1),
                    "TRACK": (self.arcade_tarmac_tracks, 1)
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 3
            ),
            GameObjectiveTemplate(
                label = "Win the race at TRACK in Class CLASS at RANK level or higher in Arcade Mode!",
                data = {
                    "CLASS": (self.arcade_classes, 1),
                    "RANK": (self.arcade_ranks, 1),
                    "TRACK": (self.arcade_tarmac_tracks, 1)
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 3
            ),
            GameObjectiveTemplate(
                label = "Stand on the podium at TRACK in Class CLASS at RANK level in Arcade Mode!",
                data = {
                    "CLASS": (self.arcade_classes, 1),
                    "RANK": (self.arcade_hard_ranks, 1),
                    "TRACK": (self.arcade_tarmac_tracks, 1)
                },
                is_time_consuming = False,
                is_difficult = True,
                weight = 3
            ),
            GameObjectiveTemplate(
                label = "Win the race at TRACK in Class CLASS at RANK level in Arcade Mode!",
                data = {
                    "CLASS": (self.arcade_classes, 1),
                    "RANK": (self.arcade_hard_ranks, 1),
                    "TRACK": (self.arcade_tarmac_tracks, 1)
                },
                is_time_consuming = False,
                is_difficult = True,
                weight = 3
            )
        ] if self.include_arcade_mode else []
    
    def get_career_objectives(self) -> List[GameObjectiveTemplate]:
        return (self.get_licence_objectives() +
                self.get_league_objectives() +
                self.get_event_objectives() +
                self.get_rally_objectives() +
                self.get_maker_objectives() +
                self.get_event_synth_objectives() +
                self.get_endurance_objectives()
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
    
    def get_league_objectives(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label = "Stand on the podium in the RACE!",
                data = {
                    "RACE": (self.gt_league_races, 1)
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 3
            ),
            GameObjectiveTemplate(
                label = "Win the RACE!",
                data = {
                    "RACE": (self.gt_league_races, 1)
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 3
            ),
            GameObjectiveTemplate(
                label = "Become the LEAGUE Champion!",
                data = {
                    "LEAGUE": (self.gt_league_series, 1)
                },
                is_time_consuming = True,
                is_difficult = False,
                weight = 3
            )
        ] if self.include_gt_league else []
    
    def get_event_objectives(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label = "Stand on the podium in the RACE!",
                data = {
                    "RACE": (self.special_events_races, 1)
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 3
            ),
            GameObjectiveTemplate(
                label = "Win the RACE!",
                data = {
                    "RACE": (self.special_events_races, 1)
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 3
            ),
            GameObjectiveTemplate(
                label = "Become the LEAGUE Champion!",
                data = {
                    "LEAGUE": (self.special_events_series, 1)
                },
                is_time_consuming = True,
                is_difficult = False,
                weight = 3
            )
        ] if self.include_special_events else []
    
    def get_rally_objectives(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label = "Win the RALLY!",
                data = {
                    "RALLY": (self.dirt_events_races, 1)
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 3
            ),
            GameObjectiveTemplate(
                label = "Win the RALLY!",
                data = {
                    "RALLY": (self.dirt_events_hard_races, 1)
                },
                is_time_consuming = False,
                is_difficult = True,
                weight = 3
            )
        ] if self.include_rally_events else []
    
    def get_maker_objectives(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label = "Win the RACE in a STYLE car!",
                data = {
                    "RACE": (self.maker_events_races, 1),
                    "STYLE": (self.maker_events_styles, 1)
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 3
            ),
            GameObjectiveTemplate(
                label = "Win the RACE in a Normal car!",
                data = {
                    "RACE": (self.maker_events_normal_only, 1)
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 3
            )
        ] if self.include_maker_events else []
    
    def get_event_synth_objectives(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label = "Stand on the podium in an Event Generator Race at RANK difficulty or higher!",
                data = {
                    "RANK": (self.arcade_hard_ranks, 1)
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 3
            ),
            GameObjectiveTemplate(
                label = "Win an Event Generator Race at RANK difficulty or higher!",
                data = {
                    "RANK": (self.event_synth_ranks, 1)
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 3
            ),
            GameObjectiveTemplate(
                label = "Stand on the podium in an Event Generator Race at RANK difficulty!",
                data = {
                    "RANK": (self.event_synth_hard_ranks, 1)
                },
                is_time_consuming = False,
                is_difficult = True,
                weight = 3
            ),
            GameObjectiveTemplate(
                label = "Win an Event Generator Race at RANK difficulty!",
                data = {
                    "RANK": (self.event_synth_hard_ranks, 1)
                },
                is_time_consuming = False,
                is_difficult = True,
                weight = 3
            ),
            GameObjectiveTemplate(
                label = "Become the Champion in an Event Generator Championship as RANK difficulty!",
                data = {
                    "RANK": (self.event_synth_long_ranks, 1)
                },
                is_time_consuming = True,
                is_difficult = True,
                weight = 3
            )
        ] if self.include_event_synth else []
    
    def get_endurance_objectives(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label = "Win the RACE!",
                data = {
                    "RACE": (self.endurances, 1)
                },
                is_time_consuming = True,
                is_difficult = False,
                weight = 3
            )
        ] if self.include_endurances else []