##  GnuBot, a program that downloads and installs GNU packages
##  Copyright (C) 2022 GnuBot

##  This program is free software: you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation, either version 3 of the License, or
##  (at your option) any later version.

##  This program is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.

##  You should have received a copy of the GNU General Public License
##  along with this program.  If not, see <https://www.gnu.org/licenses/>.
import requests

print('Beginning file download with requests')

url = 'http://raw.githubusercontent.com/gnubot/WebGet/main/webget.r'

r = requests.get(url)

with open('./webget.r', 'wb') as f:

    f.write(r.content)

# Retrieve HTTP meta-data

print(r.status_code)

print(r.headers['content-type'])

print(r.encoding)
