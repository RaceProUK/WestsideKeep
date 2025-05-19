from __future__ import annotations

from typing import List, Set

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

@dataclass
class GT3APOptions:
    gran_turismo_3_include_arcade_mode: GT3IncludeArcadeMode
    gran_turismo_3_include_career_mode: GT3IncludeCareerMode
    gran_turismo_3_career_sections: GT3CareerSections

class GT3IncludeArcadeMode(Toggle):
    """
    Allow Arcade Mode races as objectives
    """
    display_name = "Include Arcade Mode"

class GT3IncludeCareerMode(Toggle):
    """
    Allow Gran Turismo Mode races as objectives
    """
    display_name = "Include Gran Turismo Mode"

class GT3CareerSections(OptionSet):
    """
    Which parts of Gran Turismo Mode are allowed for objectives:
    - Licenses
    - Beginner League
    - Amateur League
    - Professional League
    - Endurance League
    - Rally Events
    """
    display_name = "Gran Turismo Mode Objective Areas"
    valid_keys = ["Licenses", "Beginner League", "Amateur League", "Professional League", "Endurance League", "Rally Events"]
    default = valid_keys

class GranTurismo3(Game):
    name = "Gran Turismo 3: A-Spec"
    platform = KeymastersKeepGamePlatforms.PS2
    is_adult_only_or_unrated = False
    options_cls = GT3APOptions
    
    @property
    def include_arcade_mode(self) -> bool:
        return bool(self.archipelago_options.gran_turismo_3_include_arcade_mode.value)
    
    @property
    def include_career_mode(self) -> bool:
        return bool(self.archipelago_options.gran_turismo_3_include_career_mode.value)
    
    @property
    def career_sections(self) -> Set[str]:
        return self.archipelago_options.gran_turismo_3_career_sections.value
    
    @property
    def include_licence_tests(self) -> bool:
        return "Licenses" in self.career_sections
    
    @property
    def include_beginner_league(self) -> bool:
        return "Beginner League" in self.career_sections
    
    @property
    def include_amateur_league(self) -> bool:
        return "Amateur League" in self.career_sections
    
    @property
    def include_professional_league(self) -> bool:
        return "Professional League" in self.career_sections
    
    @property
    def include_endurance_league(self) -> bool:
        return "Endurance League" in self.career_sections
    
    @property
    def include_rally_events(self) -> bool:
        return "Rally Events" in self.career_sections
    
    def arcade__tarmac_classes(self) -> List[str]:
        return ["C", "B", "A", "S"]

    def arcade_ranks(self) -> List[str]:
        return ["Easy", "Normal"]
    
    def arcade_hard_ranks(self) -> List[str]:
        return ["Hard", "Pro"]
    
    def arcade_tarmac_tracks(self) -> List[str]:
        return [
            "Apricot Hill Raceway", "Cote d'Azur", "Deep Forest Raceway",
            "Grand Valley Speedway", "Mazda Raceway Laguna Seca",
            "Mid-Field Raceway", "Rome Circuit", "Seattle Circuit",
            "Special Stage Route 5", "Special Stage Route 5 Wet",
            "Special Stage Route 11", "Super Speedway", "Test Course",
            "Tokyo R246", "Trial Mountain Circuit"
        ]
    
    def arcade_rally_tracks(self) -> List[str]:
        return ["Smokey Mountain", "Swiss Alps", "Tahiti Circuit", "Tahiti Maze"]

    def licence_tests(self) -> List[str]:
        return [f"{l}-{n}" for l in ["B", "A", "IB", "IA", "S", "R"] for n in range(1, 8)]
    
    def beginner_league_races(self) -> List[str]:
        sets = {
            "Sunday Cup": 3,
            "Clubman Cup": 3,
            "FF Challenge": 3,
            "FR Challenge": 3,
            "MR Challenge": 3,
            "4WD Challenge": 3,
            "Lightweight Sports Car Cup": 3,
            "Stars & Stripes": 4,
            "Spider & Roadster": 3,
            "80's Sports Car Cup": 3,
            "Race of NA Sports": 3,
            "Race of Turbo Sports": 3,
            "Legend of Silver Arrow": 3,
            "Evolution Meeting": 3
        }
        return [f"{series} Race {n + 1}" for series, count in sets.items() for n in range(0, count)]

    def beginner_league_series(self) -> List[str]:
        return [
            "Tourist Trophy", "Altezza Race",
            "Vitz/Yaris Race", "Type-R Meeting",
            "Beetle Cup", "Gran Turismo World Championship"
        ]
    
    def amateur_league_races(self) -> List[str]:
        sets = {
            "FF Challenge": 3,
            "FR Challenge": 3,
            "MR Challenge": 3,
            "4WD Challenge": 3,
            "Stars & Stripes": 4,
            "Boxer Spirit": 3,
            "80's Sports Car Cup": 3,
            "Race of NA Sports": 3,
            "Race of Turbo Sports": 3,
            "Race of Red Emblem": 3,
            "Legend of Silver Arrow": 3,
            "Evolution Meeting": 3
        }
        return [f"{series} Race {n + 1}" for series, count in sets.items() for n in range(0, count)]

    def amateur_league_series(self) -> List[str]:
        return [
            "Japanese Championship", "American Championship", "European Championship",
            "Gran Turismo World Championship", "German Touring Car Championship",
            "Gran Turismo All Stars", "All Japan GT Championship", "Tourist Trophy",
            "Altezza Race", "Type-R Meeting", "Dream Car Championship"
        ]
    
    def professional_league_races(self) -> List[str]:
        sets = {
            "British GT Car Cup": 3,
            "FF Challenge": 3,
            "FR Challenge": 3,
            "4WD Challenge": 3,
            "MR Challenge": 3,
            "Spider & Roadster": 3,
            "Boxer Spirit": 3,
            "Race of NA Sports": 3,
            "Race of Turbo Sports": 3,
            "Italian Avant Garde": 2,
            "Race of Red Emblem": 3,
            "Elise Trophy": 5,
            "Like the Wind": 1
        }
        return [f"{series} Race {n + 1}" for series, count in sets.items() for n in range(0, count)]

    def professional_league_series(self) -> List[str]:
        return [
            "GT World Championship", "Gran Turismo All Stars",
            "All Japan GT Championship", "Vitz/Yaris Race", "Clio Trophy",
            "Tuscan Challenge", "Dream Car Championship",
            "Polyphony Digital Cup", "Formula GT"
        ]

    def endurances(self) -> List[str]:
        return [
            "Grand Valley 300km", "Seattle 100 Miles",
            "Laguna Seca 200 Miles", "Passage to Colosseo",
            "Trial Mountain 2 Hours", "Special Stage Route 11 All-Night",
            "Roadster Endurance", "Tokyo R246 Endurance",
            "Mistral 78 Laps", "Super Speedway 150 Miles"
        ]

    def rally_events(self) -> List[str]:
        return [
            "Tahiti Challenge", "Tahiti Challenge II",
            "Tahiti Maze", "Tahiti Maze II",
            "Smokey Mountain Rally", "Smokey Mountain Rally II",
            "Alpine Rally", "Alpine Rally II",
            "Super Special Route 5", "Super Special Route 5 II",
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
            ),
            GameObjectiveTemplate(
                label = "Win the race at TRACK in Class R at RANK level or higher in Arcade Mode!",
                data = {
                    "RANK": (self.arcade_ranks, 1),
                    "TRACK": (self.arcade_rally_tracks, 1)
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 3
            ),
            GameObjectiveTemplate(
                label = "Win the race at TRACK in Class R at RANK level in Arcade Mode!",
                data = {
                    "RANK": (self.arcade_hard_ranks, 1),
                    "TRACK": (self.arcade_rally_tracks, 1)
                },
                is_time_consuming = False,
                is_difficult = True,
                weight = 3
            )
        ] if self.include_arcade_mode else []
    
    def get_career_objectives(self) -> List[GameObjectiveTemplate]:
        return (self.get_licence_objectives() +
                self.get_beginner_objectives() +
                self.get_amateur_objectives() +
                self.get_professional_objectives() +
                self.get_endurance_objectives() +
                self.get_rally_objectives()
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
    
    def get_beginner_objectives(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label = "Stand on the podium in the RACE!",
                data = {
                    "RACE": (self.beginner_league_races, 1)
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 3
            ),           
            GameObjectiveTemplate(
                label = "Win the RACE!",
                data = {
                    "RACE": (self.beginner_league_races, 1)
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 3
            ),
            GameObjectiveTemplate(
                label = "Become the LEAGUE Champion!",
                data = {
                    "LEAGUE": (self.beginner_league_series, 1)
                },
                is_time_consuming = True,
                is_difficult = False,
                weight = 3
            )
        ] if self.include_beginner_league else []
    
    def get_amateur_objectives(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label = "Stand on the podium in the RACE!",
                data = {
                    "RACE": (self.amateur_league_races, 1)
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 3
            ),           
            GameObjectiveTemplate(
                label = "Win the RACE!",
                data = {
                    "RACE": (self.amateur_league_races, 1)
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 3
            ),
            GameObjectiveTemplate(
                label = "Become the LEAGUE Champion!",
                data = {
                    "LEAGUE": (self.amateur_league_series, 1)
                },
                is_time_consuming = True,
                is_difficult = False,
                weight = 3
            )
        ] if self.include_amateur_league else []
    
    def get_professional_objectives(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label = "Stand on the podium in the RACE!",
                data = {
                    "RACE": (self.professional_league_races, 1)
                },
                is_time_consuming = False,
                is_difficult = True,
                weight = 3
            ),           
            GameObjectiveTemplate(
                label = "Win the RACE!",
                data = {
                    "RACE": (self.professional_league_races, 1)
                },
                is_time_consuming = False,
                is_difficult = True,
                weight = 3
            ),
            GameObjectiveTemplate(
                label = "Become the LEAGUE Champion!",
                data = {
                    "LEAGUE": (self.professional_league_series, 1)
                },
                is_time_consuming = True,
                is_difficult = True,
                weight = 3
            )
        ] if self.include_professional_league else []
    
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
    
    def get_rally_objectives(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label = "Beat your rival at RALLY!",
                data = {
                    "RALLY": (self.dirt_events_races, 1)
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 3
            ),
        ] if self.include_rally_events else []