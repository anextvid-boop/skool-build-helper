lines = open('index.html').read().splitlines()

hero = lines[0:71]
what_is_skool = lines[72:97]
roi = lines[98:147]
speed = lines[148:172]
services = lines[173:203]
process = lines[204:249]
about = lines[250:261]
pricing = lines[262:281]
rest = lines[282:]

# Modifications:
authority = [
  "",
  "    <!-- Authority Banner -->",
  "    <section class=\"authority-banner slide-up\" style=\"background: rgba(10, 10, 15, 0.8); border-top: 1px solid rgba(255,255,255,0.05); border-bottom: 1px solid rgba(255,255,255,0.05); padding: 2rem 0; margin-top: -2rem;\">",
  "      <div class=\"container text-center\">",
  "        <p style=\"color: #888; text-transform: uppercase; letter-spacing: 2px; font-size: 0.95rem; font-weight: 600; margin: 0;\">Trusted By Elite Creators Scaling Beyond £50k/mo</p>",
  "      </div>",
  "    </section>"
]

metric_insert = [
  "        <div style=\"text-align: center; margin-top: -1rem; margin-bottom: 3rem;\">",
  "          <span style=\"display: inline-block; padding: 0.5rem 1.5rem; background: rgba(160,32,255,0.1); border: 1px solid rgba(160,32,255,0.3); border-radius: 50px; color: var(--accent-light); font-weight: 600; font-family: var(--font-heading); letter-spacing: 1px;\">ESTIMATED TIME SAVED: 100+ HOURS</span>",
  "        </div>"
]

new_what_is_skool = [
  "    <!-- What is Skool Section -->",
  "    <section id=\"what-is-skool\" class=\"roi text-center\" style=\"padding: 6rem 0;\">",
  "      <div class=\"container slide-up\">",
  "        <h2 class=\"section-title\">Why Skool Is The Final Platform You Need</h2>",
  "        <p class=\"section-subtitle\" style=\"max-width: 800px; margin: 0 auto 2rem; font-size: 1.1rem; line-height: 1.8;\">",
  "          It isn't just a course host. It's an aggressive retention engine designed to compound your revenue.",
  "        </p>",
  "        <div class=\"grid-3\" style=\"margin-top: 3rem;\">",
  "          <div class=\"glass-card\">",
  "            <h3 style=\"color: var(--accent-color); font-family: var(--font-heading); margin-bottom: 1rem;\">Zero Churn Dynamics</h3>",
  "            <p>Community interacting with courses natively reduces dropout rates to near zero.</p>",
  "          </div>",
  "          <div class=\"glass-card\">",
  "            <h3 style=\"color: var(--accent-color); font-family: var(--font-heading); margin-bottom: 1rem;\">App Store Presence</h3>",
  "            <p>Your community lives directly on your members' phones in a highly rated, frictionless app.</p>",
  "          </div>",
  "          <div class=\"glass-card\">",
  "            <h3 style=\"color: var(--accent-color); font-family: var(--font-heading); margin-bottom: 1rem;\">Gamified Retention</h3>",
  "            <p>Leaderboards and unlockable tiers naturally incentivize members to stay subscribed for years.</p>",
  "          </div>",
  "        </div>",
  "      </div>",
  "    </section>"
]

new_pricing = [
  "    <section id=\"pricing\" class=\"pricing text-center\">",
  "      <div class=\"container slide-up\">",
  "        <h2 class=\"section-title\">Maximum Momentum</h2>",
  "        <p class=\"section-subtitle\">We only work with creators serious about scaling above £50k/mo.</p>",
  "        <div class=\"pricing-card glass-card\" style=\"border: 1px solid rgba(160,32,255,0.5); box-shadow: 0 0 40px rgba(160,32,255,0.1); position: relative; overflow: hidden;\">",
  "          <div style=\"position: absolute; top: 0; right: 0; background: var(--accent-color); color: #fff; padding: 0.5rem 3rem; font-weight: 700; font-size: 0.8rem; letter-spacing: 2px; transform: rotate(45deg) translate(25%, -200%); width: 250px;\">INVITATION ONLY</div>",
  "          <h3 style=\"font-size: 2.5rem; margin-bottom: 0.5rem;\">The Elite Build</h3>",
  "          <div class=\"price\" style=\"font-size: 1.5rem; color: var(--accent-light); margin-bottom: 1.5rem;\">Application Required</div>",
  "          <p style=\"margin-bottom: 2rem;\">Because unparalleled ROI demands a premium foundation.</p>",
  "          <ul class=\"benefits\" style=\"text-align: left; margin: 0 auto 2rem; max-width: 400px;\">",
  "            <li style=\"margin-bottom: 1rem;\">Full Skool Group Architecture Setup</li>",
  "            <li style=\"margin-bottom: 1rem;\">Custom High-Converting Landing Pages</li>",
  "            <li style=\"margin-bottom: 1rem;\">Professional Video Course Editing</li>",
  "            <li style=\"margin-bottom: 1rem;\">Intelligent Backend AI Automations</li>",
  "            <li style=\"margin-bottom: 1rem; color: var(--accent-light); font-weight: 700;\">Direct 1-on-1 Strategic Access with Jahroinimo</li>",
  "          </ul>",
  "          <a href=\"apply.html\" class=\"btn btn-primary lg button-shine mt-4\">Apply For The Elite Build</a>",
  "          <a href=\"https://wa.me/447538068550\" target=\"_blank\" class=\"btn btn-outline\" style=\"border-width: 1px; color: #25D366; border-color: rgba(37, 211, 102, 0.4); margin-top: 1rem; display: block; width: 100%; text-align: center;\">Message on WhatsApp Instead</a>",
  "        </div>",
  "      </div>",
  "    </section>"
]

s_out = []
for l in services:
    s_out.append(l)
    if "Everything You Need" in l:
        s_out.extend(metric_insert)

new_order = hero + authority + speed + s_out + process + roi + new_what_is_skool + new_pricing + about + rest

with open('index.html', 'w') as f:
    f.write("\n".join(new_order) + "\n")
