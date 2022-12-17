# AoC-2022

My solutions for [Advent of Code 2022](https://adventofcode.com/2022).

## Advent Calendar

<div align="center">
<table>
    <thead>
        <tr>
            <th colspan="7"><div align="center">December 2022</div></th>
        </tr>
        <tr>
            <th align="center">Sun</th>
            <th align="center">Mon</th>
            <th align="center">Tue</th>
            <th align="center">Wed</th>
            <th align="center">Thu</th>
            <th align="center">Fri</th>
            <th align="center">Sat</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center"></td>
            <td align="center"></td>
            <td align="center"></td>
            <td align="center"></td>
            <td align="center"><a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/day/01/program.py">1</a></td>
            <td align="center"><a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/day/02/program.py">2</a></td>
            <td align="center"><a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/day/03/program.py">3</a></td>
        </tr>
        <tr>
            <td align="center"><a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/day/04/program.py">4</a></td>
            <td align="center"><a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/day/05/program.py">5</a></td>
            <td align="center"><a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/day/06/program.py">6</a></td>
            <td align="center"><a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/day/07/program.py">7</a></td>
            <td align="center"><a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/day/08/program.py">8</a></td>
            <td align="center"><a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/day/09/program.py">9</a></td>
            <td align="center"><a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/day/10/program.py">10</a></td>
        </tr>
        <tr>
            <td align="center"><a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/day/11/program.py">11</a></td>
            <td align="center"><a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/day/12/program.py">12</a></td>
            <td align="center"><a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/day/13/program.py">13</a></td>
            <td align="center"><a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/day/14/program.py">14</a></td>
            <td align="center"><a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/day/15/program.py">15</a></td>
            <td align="center"><!--<a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/day/16/program.py">16</a>-->16</td>
            <td align="center"><!--<a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/day/17/program.py">17</a>-->17</td>
        </tr>
        <tr>
            <td align="center"><!--<a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/day/18/program.py">18</a>-->18</td>
            <td align="center"><!--<a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/day/19/program.py">19</a>-->19</td>
            <td align="center"><!--<a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/day/20/program.py">20</a>-->20</td>
            <td align="center"><!--<a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/day/21/program.py">21</a>-->21</td>
            <td align="center"><!--<a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/day/22/program.py">22</a>-->22</td>
            <td align="center"><!--<a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/day/23/program.py">23</a>-->23</td>
            <td align="center"><!--<a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/day/24/program.py">24</a>-->24</td>
        </tr>
        <tr>
            <td align="center"><!--<a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/day/25/program.py">25</a>-->25</td>
            <td align="center"></td>
            <td align="center"></td>
            <td align="center"></td>
            <td align="center"></td>
            <td align="center"></td>
            <td align="center"></td>
        </tr>
    </tbody>
</table>
<small>
    Note: The link always points to the code in `main` branch.
</small>
</div>

## Structure

Each day is stored in its own directory inside `day` directory, with the input in `input.txt` and the solution in `solution.py`.

```
.
├── config.json
├── generate.py
├── LICENSE
├── README.md
└── day
     ├── 00
     │   ├── input.txt
     │   └── solution.py
     ├── 01
     │   ├── input.txt
     │   └── solution.py
     ├── ...
     └── 25
         ├── input.txt
         └── solution.py
```

## Usage

First, set up `config.json`.

To **generate a directory** for a new day, run
```sh
$ ./generate.sh <day> <problem title>
$ ./generate.sh 1 "Calorie Counting"  # Example
```
This will create a copy of template directory `00/` and change the name and contents of the files to match the day and problem title.

To **run the solution** for a day, run
```sh
$ python3 day/<day>/solution.py < day/<day>/input.txt
$ python3 day/01/solution.py < day/01/input.txt  # Example
```
