from dataclasses import dataclass

@dataclass
class Material:
    name: str
    u_value: str
    conductivity: float
    density: float
    roughness: str
    specific_heat: float
    thermal_abstoptance: float
    solar_abstoptance: float
    visible_abstoptance: float
    thickness_wall: float
    thickness_ground: float
    thickness_roof: float
    price_wall: float
    price_ground: float
    price_roof: float
    embodied_emissions: float

materials = {
    "hempcrete_0.1": Material(
        "Hempcrete",
        0.1,
        0.07,
        170,
        "Rough",
        1870,
        0.9,
        0.6,
        0.6,
        0.682,
        0.671,
        0.676,
        372.0,
        372.0,
        372.0,
        5,

    ),
    "hempcrete_0.25": Material(
        "Hempcrete",
        0.25,
        0.07,
        170,
        "Rough",
        1870,
        0.9,
        0.6,
        0.6,
        0.262,
        0.251,
        0.256,
        409.0,
        409.0,
        409.0,
        5,
    ),
        "eps_0.1": Material(
        "EPS",
        0.1,
        0.03,
        30,
        "Rough",
        1500,
        0.9,
        0.6,
        0.6,
        0.292,
        0.288,
        0.290,
        368.3,
        368.3,
        368.3,
        229.2,

    ),
        "eps_0.25": Material(
        "EPS",
        0.25,
        0.03,
        30,
        "Rough",
        1500,
        0.9,
        0.6,
        0.6,
        0.112,
        0.108,
        0.110,
        501.7,
        555.0,
        501.7,
        229.2,

    ),
        "rockwool_0.1": Material(
        "Rockwool",
        0.1,
        0.035,
        38,
        "Rough",
        870,
        0.9,
        0.6,
        0.6,
        0.341,
        0.336,
        0.338,
        338.8,
        338.8,
        338.8,
        42.9,

    ),
        "rockwool_0.25": Material(
        "Rockwool",
        0.25,
        0.035,
        38,
        "Rough",
        870,
        0.9,
        0.6,
        0.6,
        0.131,
        0.126,
        0.128,
        410.7,
        385.0,
        385.0,
        42.9,

    ),
        "straw_0.1": Material(
        "Straw",
        0.1,
        0.066,
        105,
        "Rough",
        2000,
        0.9,
        0.6,
        0.6,
        0.643,
        0.633,
        0.638,
        164.3,
        164.3,
        164.3,
        -120.1,

    ),
        "straw_0.25": Material(
        "Straw",
        0.25,
        0.066,
        105,
        "Rough",
        2000,
        0.9,
        0.6,
        0.6,
        0.247,
        0.237,
        0.242,
        430.0,
        430.0,
        430.0,
        -120.1,

    ),
        "woodfibre_0.1": Material(
        "Woodfibre",
        0.1,
        0.038,
        104,
        "Rough",
        2100,
        0.9,
        0.6,
        0.6,
        0.370,
        0.364,
        0.367,
        650.0,
        650.0,
        650.0,
        -173.3,

    ),
        "woodfibre_0.25": Material(
        "Woodfibre",
        0.25,
        0.038,
        104,
        "Rough",
        2100,
        0.9,
        0.6,
        0.6,
        0.142,
        0.136,
        0.139,
        756.3,
        908.3,
        908.3,
        -173.3,

    ),
}

