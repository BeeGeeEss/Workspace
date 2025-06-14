# 🔮✨ Natal Chart Generator ✨🔮

> The Natal Chart Generator is a simple command-line  application used to identify the position of the planets at the time of the users birth. This application generates an SVG chart for the user to keep.

## Background & Planning

In preparation for building this app, an analysis was conducted to compare astrological/natal Python libraries. Most of these libraries are based on the Swiss Ephemeris library (pyswisseph) which calculates astrological data and the Olsen Timezone Database (pytz) which enables timezone calculations and corrections.

From the list of relevant libraries - two were selected and compared (Kerykeion | Natal) with Kerykeion being a better fit for this application due to it's ability to input latitude, longitude and timezone, rather than needing to convert timezones manually.

## Installation & Requirements

*Kerykeion* requires Python 3.9 or higher. *Colorama* will work on a range of python versions which includes 3.9/3.10.

### - Installation of Application -

Clone the below repository or open the folder if a local copy has been provided:

```py
git clone https://github.com/BeeGeeEss/natal_chart_app
cd ...
```

Create and activate a virtual environment:

```py
python -m venv venv
source venv/bin/activate
```

Run the script:

```py
python ....py
```

### - Installation of Libraries -

Both libraries can be installed with pip:

```py
pip install kerykeion
```

```py
pip install colorama
```

If you face any issues with components of the Kerykeion library (functions not running as predicted), you can manually install pyswisseph, pytz or use the standard library for datetime:

```py
pip install pyswisseph
```

```py
pip install pytz
```

## Basic Usage

## SVG Generation

## Help or Troubleshooting


## Librabries & Licencing

This project is licensed under the Massachusetts Institute of Technology (MIT) License. See the [LICENSE](./LICENSE) file for more details.

It also uses the following third-party libraries:

- Colorama - Licensed under the Berkeley Software Distribution (BSD) License. See [Colorama's license](https://github.com/tartley/colorama/blob/main/LICENSE.txt).
- Kerykeion - Licensed under Massachusetts Institute of Technology (MIT) License. See [Kerykeion's license](https://github.com/rwolfog/pyKerykeion/blob/main/LICENSE).

### - Ethical Considerations -

Kerykeion and Colorama are both licensed under permissive, open-source licenses which allow use, modification and redistribution. MIT and BSD licenses are compatible with eachother.

MIT Licenses Require:

> The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

BSD-3-Clause Licenses Require:

> 1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
> 2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
> 3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

<u>This application has only imported these libraries via pip, it has not modified or redistributed source code. No promotional products are in use.</u>

Important Note: If the Pyswissemph library is imported for use with this application (as opposed to just importing the Kerykeion library), Pyswissemph is licensed under GNU Affero General Public License (AGPL). AGPL licenses are less permissive and are referred to as copyleft open-source licenses. However, this application would be using Pyswissemph ONLY as a library imported via pip and therefore it would be used in its most permissive state. This means that the application can still use an MIT license. If this application was modifying pyswissemph source code, consideration would need to be taken to also license the application under AGPL. Modified source code would also need to be made available to anyone who interacts with the software.

See [Python's extension to the Swiss Ephemeris' license](https://github.com/astrorigin/pyswisseph/blob/master/LICENSE.txt)