# AoC-2022

My solutions for [Advent of Code 2022](https://adventofcode.com/2022).

## Advent Calendar

<div>
<table style="text-align:center">
    <thead>
        <tr>
            <th colspan="7" style="text-align:center">December 2022</th>
        </tr>
        <tr>
            <th>Sun</th>
            <th>Mon</th>
            <th>Tue</th>
            <th>Wed</th>
            <th>Thu</th>
            <th>Fri</th>
            <th>Sat</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td><a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/01/program.py">1</a></td>
            <td><a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/02/program.py">2</a></td>
            <td><a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/03/program.py">3</a></td>
        </tr>
        <tr>
            <td><a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/04/program.py">4</a></td>
            <td><a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/05/program.py">5</a></td>
            <td><a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/06/program.py">6</a></td>
            <td><a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/07/program.py">7</a></td>
            <td><a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/08/program.py">8</a></td>
            <td><a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/09/program.py">9</a></td>
            <td><!--<a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/10/program.py">10</a>-->10</td>
        </tr>
        <tr>
            <td><!--<a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/11/program.py">11</a>-->11</td>
            <td><!--<a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/12/program.py">12</a>-->12</td>
            <td><!--<a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/13/program.py">13</a>-->13</td>
            <td><!--<a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/14/program.py">14</a>-->14</td>
            <td><!--<a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/15/program.py">15</a>-->15</td>
            <td><!--<a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/16/program.py">16</a>-->16</td>
            <td><!--<a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/17/program.py">17</a>-->17</td>
        </tr>
        <tr>
            <td><!--<a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/18/program.py">18</a>-->18</td>
            <td><!--<a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/19/program.py">19</a>-->19</td>
            <td><!--<a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/20/program.py">20</a>-->20</td>
            <td><!--<a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/21/program.py">21</a>-->21</td>
            <td><!--<a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/22/program.py">22</a>-->22</td>
            <td><!--<a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/23/program.py">23</a>-->23</td>
            <td><!--<a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/24/program.py">24</a>-->24</td>
        </tr>
        <tr>
            <td><!--<a href="https://codeberg.org/kimerikal/AoC-2022/src/branch/main/25/program.py">25</a>-->25</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
    </tbody>
</table>
<small>
    Note: The link always points to the code in `main` branch.
</small>
</div>

## Structure

Each day is in its own directory, with the input in `input.txt` and the solution in `solution.py`.

```
.
├── config.json
├── generate.py
├── LICENSE
├── README.md
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
$ python3 <day>/solution.py < <day>/input.txt
$ python3 01/solution.py < 01/input.txt  # Example
```
