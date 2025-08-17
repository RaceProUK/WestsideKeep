#v3

from __future__ import annotations

from typing import List, Set

from dataclasses import dataclass

from Options import DefaultOnToggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

@dataclass
class GT1APOptions:
    gran_turismo_include_arcade_mode: GT1IncludeArcadeMode
    gran_turismo_include_career_mode: GT1IncludeCareerMode
    gran_turismo_career_sections: GT1CareerSections

class GT1IncludeArcadeMode(DefaultOnToggle):
    """
    Allow Arcade Mode races as objectives
    """
    display_name = "Include Arcade Mode"

class GT1IncludeCareerMode(DefaultOnToggle):
    """
    Allow Gran Turismo Mode races as objectives
    """
    display_name = "Include Gran Turismo Mode"

class GT1CareerSections(OptionSet):
    """
    Which parts of Gran Turismo Mode are allowed for objectives:
    - Licenses
    - GT League
    - Special Events
    - Spot Races
    - Endurance
    """
    display_name = "Gran Turismo Mode Objective Areas"
    valid_keys = ["Licenses", "GT League", "Special Events", "Spot Races", "Endurance"]
    default = valid_keys

class GranTurismo(Game):
    name = "Gran Turismo"
    platform = KeymastersKeepGamePlatforms.PS1
    is_adult_only_or_unrated = False
    options_cls = GT1APOptions
    
    @property
    def include_arcade_mode(self) -> bool:
        return bool(self.archipelago_options.gran_turismo_include_arcade_mode.value)
    
    @property
    def include_career_mode(self) -> bool:
        return bool(self.archipelago_options.gran_turismo_include_career_mode.value)
    
    @property
    def career_sections(self) -> Set[str]:
        return self.archipelago_options.gran_turismo_career_sections.value
    
    @property
    def include_licence_tests(self) -> bool:
        return "Licenses" in self.career_sections
    
    @property
    def include_gt_league(self) -> bool:
        return "GT League" in self.career_sections
    
    @property
    def include_special_events(self) -> bool:
        return "Special Events" in self.career_sections
    
    @property
    def include_spot_races(self) -> bool:
        return "Spot Races" in self.career_sections
    
    @property
    def include_endurances(self) -> bool:
        return "Endurance" in self.career_sections
    
    def arcade_classes(self) -> List[str]:
        return ["C", "B", "A"]
    
    def arcade_ranks(self) -> List[str]:
        return ["Easy", "Normal"]
    
    def arcade_hard_ranks(self) -> List[str]:
        return ["Hard"]
    
    def arcade_tracks(self) -> List[str]:
        return [
            "High Speed Ring", "Trial Mountain Circuit", "Grand Valley East", "Clubman Stage Route 5",
            "Autumn Ring", "Deep Forest", "Special Stage Route 5", "Grand Valley Speedway"
         ]
    
    def licence_tests(self) -> List[str]:
        return [f"{l}-{n}" for l in ["B", "A", "IA"] for n in range(1, 9)]
    
    def gt_league(self) -> List[str]:
        return ["Sunday Cup", "Clubman Cup", "Gran Turismo Cup", "Gran Turismo World Cup"]
    
    def special_events(self) -> List[str]:
        return [
            "FF Challenge", "FR Challenge", "4WD Challenge", "Lightweight Sports Battle Stage",
            "US-Japan Sports Car Championship", "Anglo-Japanese Sports Car Championship", "Anglo-American Sports Car Championship",
            "Megaspeed Cup", "Normal Car World Speed Contest", "Hard-Tuned Car Speed Contest"
        ]
    
    def spot_race_tracks(self) -> List[str]:
        return ["High Speed Ring", "Grand Valley East", "Autumn Ring Mini", "Trial Mountain Circuit", "Deep Forest"]
    
    def endurances(self) -> List[str]:
        return ["Grand Valley 300km", "Special Stage Route 11 All-Night 1", "Special Stage Route 11 All-Night 2"]
    
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
                    "TRACK": (self.arcade_tracks, 1)
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
                    "TRACK": (self.arcade_tracks, 1)
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
                    "TRACK": (self.arcade_tracks, 1)
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
                    "TRACK": (self.arcade_tracks, 1)
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
                self.get_spot_race_objectives() +
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
                label = "Become the LEAGUE Champion!",
                data = {
                    "LEAGUE": (self.gt_league, 1)
                },
                is_time_consuming = True,
                is_difficult = False,
                weight = 3
            )
        ] if self.include_gt_league else []
    
    def get_event_objectives(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label = "Become the EVENT Champion!",
                data = {
                    "EVENT": (self.special_events, 1)
                },
                is_time_consuming = True,
                is_difficult = False,
                weight = 3
            )
        ] if self.include_special_events else []
    
    def get_spot_race_objectives(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label = "Stand on the podium in a Spot Race at TRACK!",
                data = {
                    "TRACK": (self.spot_race_tracks, 1)
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 3
            ),
            GameObjectiveTemplate(
                label = "Win a Spot Race at TRACK!",
                data = {
                    "TRACK": (self.spot_race_tracks, 1)
                },
                is_time_consuming = False,
                is_difficult = False,
                weight = 3
            )
        ] if self.include_spot_races else []
    
    def get_endurance_objectives(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label = "Win the EVENT!",
                data = {
                    "EVENT": (self.endurances, 1)
                },
                is_time_consuming = True,
                is_difficult = False,
                weight = 3
            )
        ] if self.include_endurances else []