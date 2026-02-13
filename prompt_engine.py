class PromptEngine:
    """
    Emotion-driven, environment-only prompt engine.
    Scene-specific, SD 1.5 optimized.
    """

    def __init__(self):
        self.emotion_scenes = {

            "happy": {
                "low": (
                    "open green field, soft sunlight, calm atmosphere"
                ),
                "medium": (
                    "wide open meadow filled with colorful flowers, "
                    "bright sunlight, clear blue sky, lively nature"
                ),
                "high": (
                    "vast flower-filled landscape, intense sunlight, "
                    "vivid colors, blooming nature everywhere, "
                    "pure joy, energetic bright atmosphere"
                )
            },

            "sad": {
                "low": (
                    "empty landscape, muted colors, quiet loneliness"
                ),
                "medium": (
                    "rainy environment, soft fog, "
                    "cold desaturated colors, melancholic silence"
                ),
                "high": (
                    "endless rain, heavy fog, dark horizon, "
                    "cold blue-gray palette, emotional heaviness"
                )
            },

            "angry": {
                "low": (
                    "dark heavy clouds, rising wind, tense atmosphere"
                ),
                "medium": (
                    "violent thunderstorm, frequent lightning bolts, "
                    "dark sky, strong wind motion, dramatic contrast"
                ),
                "high": (
                    "violent lightning bolts, explosive clouds, "
                    "extreme contrast, chaotic sky, "
                    "high energy atmosphere"    
                )
            },

            "fear": {
                "low": (
                    "dark narrow space, limited visibility"
                ),
                "medium": (
                    "dense fog, abandoned environment, "
                    "uneasy silence, hidden threats"
                ),
                "high": (
                    "claustrophobic environment, extreme darkness, "
                    "oppressive fog, unknown danger, "
                    "psychological horror atmosphere"
                )
            },

            "neutral": {
                "low": (
                    "plain empty environment, flat lighting, no mood emphasis"
                ),
                "medium": (
                    "simple everyday landscape, neutral colors, "
                    "balanced light, ordinary atmosphere"
                ),
                "high": (
                    "minimal environment, flat colors, "
                    "no dramatic lighting, calm and uneventful scene"
                )
            },

            "surprise": {
                "low": (
                    "unusual object floating in the sky, subtle curiosity"
                ),
                "medium": (
                    "sudden futuristic light beam, "
                    "unexpected energy source, dramatic moment"
                ),
                "high": (
                    "futuristic phenomenon, massive energy portal, "
                    "unknown technology in the sky, "
                    "bright unnatural colors, awe and shock"
                )
            }
        }

        self.style_map = {

            "Realistic": (
                "cinematic landscape photography, realistic terrain, "
                "atmospheric depth, natural lighting"
            ),

            "Anime": {

                "happy": {
                    "low": (
                        "quiet anime countryside, soft sunlight, "
                        "peaceful atmosphere"
                    ),
                    "medium": (
                        "bright anime landscape, blue sky, fluffy clouds, "
                        "warm joyful mood"
                    ),
                    "high": (
                        "vibrant anime scenery, intense sunlight, "
                        "dreamy colorful sky"
                    )
                },

                "sad": {
                    "low": (
                        "empty anime street, cloudy sky"
                    ),
                    "medium": (
                        "rainy anime town, soft reflections, "
                        "melancholic calm mood"
                    ),
                    "high": (
                        "lonely anime landscape, heavy rain, "
                        "emotional dramatic lighting"
                    )
                },

                "angry": {
                    "low": (
                        "dark anime clouds, tense sky"
                    ),
                    "medium": (
                        "stormy anime environment, dramatic lighting"
                    ),
                    "high": (
                        "anime natural disaster scene, intense wind, "
                        "dramatic cinematic tension"
                    )
                },

                "fear": {
                    "low": (
                        "quiet anime forest at night"
                    ),
                    "medium": (
                        "foggy anime village, moonlight, eerie silence"
                    ),
                    "high": (
                        "abandoned anime house, dim light, "
                        "psychological tension"
                    )
                },

                "neutral": {
                    "low": (
                        "simple anime landscape, neutral sky"
                    ),
                    "medium": (
                        "balanced anime environment, soft lighting"
                    ),
                    "high": (
                        "clean anime background, minimal details"
                    )
                },

                "surprise": {
                    "low": (
                        "unexpected object in anime sky"
                    ),
                    "medium": (
                        "sudden light burst, anime style clouds"
                    ),
                    "high": (
                        "spectacular anime sky phenomenon, "
                        "awe inspiring moment"
                    )
                }
            },

            "Pixel Art": {

                "happy": {
                    "low": (
                        "peaceful pixel village, green grass"
                    ),
                    "medium": (
                        "colorful pixel landscape, flowers, sunny sky"
                    ),
                    "high": (
                        "vibrant pixel world, bright colors, joyful scene"
                    )
                },

                "sad": {
                    "low": (
                        "empty pixel field, gray sky"
                    ),
                    "medium": (
                        "rainy pixel town, muted colors"
                    ),
                    "high": (
                        "foggy pixel forest, lonely atmosphere"
                    )
                },

                "angry": {
                    "low": (
                        "dark pixel clouds"
                    ),
                    "medium": (
                        "pixel storm, red sky"
                    ),
                    "high": (
                        "pixel volcano, lava, fire tiles"
                    )
                },

                "fear": {
                    "low": (
                        "dark pixel forest"
                    ),
                    "medium": (
                        "foggy pixel dungeon corridor"
                    ),
                    "high": (
                        "abandoned pixel dungeon, dim torches"
                    )
                },

                "neutral": {
                    "low": (
                        "simple pixel terrain"
                    ),
                    "medium": (
                        "balanced pixel overworld map"
                    ),
                    "high": (
                        "clean pixel environment, minimal tiles"
                    )
                },

                "surprise": {
                    "low": (
                        "unexpected pixel object"
                    ),
                    "medium": (
                        "sudden pixel light effect"
                    ),
                    "high": (
                        "pixel sky event, falling meteor"
                    )
                }
            },

            "Cyberpunk": {
                "happy": {
                    "low": (
                        "calm cyberpunk street, soft neon reflections, "
                        "quiet night city"
                    ),
                    "medium": (
                        "neon city street, colorful holographic signs, "
                        "warm cyberpunk lights, lively atmosphere"
                    ),
                    "high": (
                        "vibrant cyberpunk city, glowing neon skyscrapers, "
                        "celebration lights, energetic futuristic mood"
                    )
                },

                "sad": {
                    "low": (
                        "empty cyberpunk alley, dim neon lights, wet pavement"
                    ),
                    "medium": (
                        "rainy cyberpunk street, flickering signs, "
                        "lonely futuristic atmosphere"
                    ),
                    "high": (
                        "abandoned cyberpunk district, heavy rain, "
                        "broken holograms, deep melancholy"
                    )
                },

                "angry": {
                    "low": (
                        "tense cyberpunk street, red warning lights"
                    ),
                    "medium": (
                        "cyberpunk riot aftermath, flashing alarms, "
                        "red neon glow, aggressive lighting"
                    ),
                    "high": (
                        "cyberpunk city in chaos, system failure, "
                        "exploding transformers, red emergency lights"
                    )
                },

                "fear": {
                    "low": (
                        "dark cyberpunk alley, low visibility, shadows"
                    ),
                    "medium": (
                        "foggy cyberpunk corridor, malfunctioning lights, "
                        "uneasy tension"
                    ),
                    "high": (
                        "abandoned cyberpunk underground, flickering lights, "
                        "dense fog, psychological tension"
                    )
                },

                "neutral": {
                    "low": (
                        "quiet cyberpunk street, neutral lighting"
                    ),
                    "medium": (
                        "balanced cyberpunk city view, soft neon colors"
                    ),
                    "high": (
                        "minimal cyberpunk environment, clean futuristic architecture"
                    )
                },

                "surprise": {
                    "low": (
                        "unexpected hologram glitch in cyberpunk street"
                    ),
                    "medium": (
                        "sudden power surge, bright neon flash"
                    ),
                    "high": (
                        "massive holographic projection in the sky, "
                        "spectacular futuristic event"
                    )
                }
            }
        }

        self.style_lock = {
            "Realistic": [
                "photorealistic",
                "cinematic photography",
                "real world lighting",
                "DSLR quality"
            ],

            "Anime": [
                "anime style",
                "anime background art",
                "hand drawn",
                "clean lineart",
                "flat shading",
                "studio ghibli inspired",
                "no realism",
                "no photorealism"
            ],

            "Pixel Art": [
                "pixel art",
                "8-bit style",
                "16-bit game background",
                "low resolution pixel grid",
                "hard pixel edges",
                "no smooth shading",
                "no realism",
                "no photorealism"
            ],

            "Cyberpunk": [
                "cyberpunk style",
                "futuristic cityscape",
                "neon lights",
                "high contrast lighting",
                "sci-fi environment",
                "blade runner inspired"
            ]
        }

    def _level(self, value):
        if value < 35:
            return "low"
        elif value < 70:
            return "medium"
        else:
            return "high"

    def generate(self, emotions: dict, style: str) -> str:
        dominant = max(emotions, key=emotions.get)
        level = self._level(emotions[dominant])

        prompt_parts = []

        style_data = self.style_map.get(style)

        # STYLE DICT (Anime / Cyberpunk / Pixel)
        if isinstance(style_data, dict):
            prompt_parts.append(
                style_data[dominant][level]
            )
        else:
            # REALISTIC vb.
            prompt_parts.append(style_data)
            prompt_parts.append(
                self.emotion_scenes[dominant][level]
            )
        
        prompt_parts.extend(self.style_lock.get(style, []))
        prompt_parts.extend([
            "environment only",
            "no people",
            "no humans",
            "cinematic lighting",
            "clean composition",
            "high quality",
            "stable diffusion 1.5",
            "single scene",
            "one environment",
            "wide angle view",
            "no split scene",
            "no collage",
            "no multiple panels",
            "no multiple scenes",
            "centered composition",
            "landscape photography framing"
        ])

        return ", ".join(prompt_parts)
