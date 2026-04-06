# Commment Analyzer for Ecamm

### Vidoe Demo: [here](https://youtu.be/G-QWKP7ouyE)

### Disclaimer

I used Grammarly to help me with the orthography and grammar, since English isn't my first language. The content of this file is still written entirely by me.

### Description

Ecamm is a Mac software for live streaming. During a Live Stream, people can put messages in the chat. The messages get stored in a SubRip File. With the Comment Analyser for Ecamm, you can collect and analyse these chats.

### Deciding the scope

This is my final project for the Harward course: "CS50's Introduction to Programming with Python". My goals for the project were:

- Fullfilling the course requierements
- Applying and practicing what I've learned
- Challenging myself
- Finishing in a resonable time
- Build something that is useful to me and potentially others

These goals guided the scope of the project. It can't be too big in order to complete it in a resonable time. It still needs to be complete enough to be useful.

I decided the scope with the **Minimal Viable Product** (MVP) strategy. It is described in [Wikipedia](https://en.wikipedia.org/wiki/Minimum_viable_product).

#### MVP Features:

- Reading the SubRip files from the programms subfolder `/srt/`.
- Parsing the files and extracting:
    - the name of the Stream from the file name
    - the time, chatter, and message from the file content
- Writing the results in a `csv` file in the programms subfolder `/out/`.
- Creating a wordcloud from the messages in a `png` file in the programs subfolder `/out/`.
- Create a list of the top 10 words, chatters, and streams, and `print` it to the `terminal`.

### Features for future releases:

- Saving the imported data in a database
- Letting the user choose the directory for the import, and the directory and filename for the output.
- Building a Streamlit web page, so people can use the tool out of the box.


### Format of the content of the `srt` files from Ecamm

Live chat messages are stored in a SubRip file, with the `.srt` extension. The format is described in [Wikipedia](https://en.wikipedia.org/wiki/SubRip).

Specific to Ecamm:

- The start time is set to when Ecamm got the chat message (relative to the start of the stream). The end time is always 5 seconds after the start time.

- The text is always on one line and is divided by a `:` into the chatter and the chat message:

    - chatter:

        The name of the person sending the chat. It may be prefixed with a `@`, but this is not always the case.

    - message

        This contains the text, that was sent. **Caution:** there may be additional `:` in the message and the message can be empty.

- The file ends with two blank lines.

**Example:**

```
1
00:02:06,000 --> 00:02:11,000
@FishstickUSA: Hello Markus

2
00:02:22,000 --> 00:02:27,000
@eaglevp: Hi Phillip
```

#### Parsing the `.srt` File

There are 4 types of lines to parse:

- **number:** check for an integer and save as `number`.
- **time:** check the starting time (hh:mm:ss) and save as `time`
- **text:** split at the first ":" into chatter and message:
    - **chatter:** ignore the optinal `@` at the start and save as `chatter`
    - **message:** ignore the leading blank, accept empty message. Save as `message`
 **blank line:** do nothing (at the end of the file is one additional blank line)

# The program (main)

- Getting the input directory for the `.srt` Files.
- Writing the directory to the Terminal.
- Getting the output directory.
- Writing the directory to the Terminal.
- Getting the files from the input directory.
- Getting all chats.
- Exit if no chats were fetched.
- Writing top 10 words to the terminal (formatted with `tabulate`).
- Writing top 10 chatters to the terminal (formatted with `tabulate`).
- Writing top 10 streams to the terminal (formatted with `tabulate`).
- Writing a message to the terminal stating that the chats are saved to a `.csv` File.
- Writing  `chats.csv` to the output directory.
- Writing a message to the terminal stating that the wordcloud is created.
- Writing  `wordcloud.png` to the output directory.


## Example output (Terminal)

```
Input directory for the .srt files: ./srt/
Output directory: ./out/

Parsing 150 files...
Can't parse file Test on 2021-12-23 at 22.59.srt, invalid number of lines
Can't parse file Test on 2026-01-02 at 12.57.srt, first error: line 6

Top words:

  Rank  Word         #
------  --------  ----
     1  Markus    1579
     2  Lala       523
     3  great      489
     4  Hello      445
     5  Yes        445
     6  everyone   441
     7  love       424
     8  Ana        404
     9  live       394
    10  will       374

Top chatters:

  Rank  Chatter                                      Chats
------  -----------------------------------------  -------
     1  Mommy Guide Inc                               3641
     2  Animal Paradise - Communication & Healing      978
     3  Eaglevp                                        901
     4  Ellie Calhoun                                  647
     5  Tech Troublemaker                              611
     6  Ana Zugheri - Faith 52                         530
     7  Cheryl Wolf                                    490
     8  Ana Zugheri - Faith52                          427
     9  Sammy Super Star                               384
    10  Kali Co                                        302

Top streams

  Rank  Stream                                                       Chats
------  ---------------------------------------------------------  -------
     1  Live Stream on 2022-09-02 at 21.56                             652
     2  Live Stream on 2022-02-24 at 21.56                             288
     3  Live Stream on 2022-08-18 at 21.57                             268
     4  Live Stream on 2021-09-02 at 21.56                             264
     5  Live Stream on 2021-10-07 at 21.56                             256
     6  Markus Schaub and Markus Schaub on 2024-04-25 at 21.59.19      222
     7  Markus Schaub on 2023-04-20 at 21.56.39                        218
     8  Markus Schaub on 2023-05-11 at 21.55.20                        217
     9  Live Stream on 2021-11-18 at 21.56                             206
    10  Markus Schaub on 2023-08-10 at 21.56.34                        204

Writing chats to ./out/chats.csv ...
Writing wordcloud to ./out/wordcloud.png ...
done!
```

## Example output (`chats.csv`)

```
Stream,Number,Time,Chatter,Message
Markus Schaub on 2023-05-11 at 21.55.20,1,00:00:39,Mommy Guide Inc,And here we go!
Markus Schaub on 2023-05-11 at 21.55.20,2,00:01:44,Mommy Guide Inc,Awesome dancing Markus & Stan!
Markus Schaub on 2023-05-11 at 21.55.20,3,00:01:53,Sammy Super Star,Hey everyone
Markus Schaub on 2023-05-11 at 21.55.20,4,00:02:21,Mommy Guide Inc,Hi Sammy!!!!
Markus Schaub on 2023-05-11 at 21.55.20,5,00:02:49,Kali ,heyo!!!
Markus Schaub on 2023-05-11 at 21.55.20,6,00:02:58,Mommy Guide Inc,💃 💃
```

## Example output (wordcloud)

![image of the wordcloud](./out/example_wordcloud.png)

# The functions

## Get directory

`def get_directory(type: str = "srt") -> str`

Getting the directories for:
- the `.srt` files to parse
- the place to write the output files (`chats.csv` and `wordcloud.png`)

The directories are hardcoded for now. But it's encapsulated into a function, so it can be fixed easily later.

If the directory does not exist, the program exits.

## Get the paths to the `.srt` files

`def get_paths(directory: str) -> List[str]`

Getting all the `.srt` files from the directory.

## Reading the files

`def read_files(paths: List[str]) -> List[Dict]`

For each file:
- Call the `parse_file` function with the filename and all lines of the file.
- In case of a parsing error, print that error to the terminal.
- If parsed successfully, collect all the chats.

Returns the chats.

## Parsing the file

`def parse_file(file_name: str, lines: List[str]) -> List[Dict]`

### Validating file lenght

The file needs to have 1 to n blocks of 4 lines plus one additional blank line. If this is not true, a `ValueError` is raised. The filename and the reason are provided in the error message.

### Extracting the values

The File gets parsed in steps of four lines:

- The number of the chat is extracted with the function `parse_number`.
- The time is extracted with the function `parse_time`.
- The chatter and the message are extracted with the function `parse_message`.
- The fourth line (the blank) gets ignored.

### Saving valid chats:

If the number, the time, and the chatter have values, the chat got successfully parsed. The message can be empty. All values get stored in a dictionary. Additionally, the stream name (the filename without the suffix) is written in the dictionary.

**Example:**

```
{
    "Stream": "Test on 2026-01-01 at 12.56",
    "Number": "1",
    "Time": "00:02:22",
    "Chatter": "Kali Co",
    "Message": "EEEEEP!!! so excited for this!!! ❤️",
}
```

### Handling invalid chats

If the chat can't be parsed, the entire file gets discarded. This includes already parsed chats for this file. A `ValueError` is raised. The filename and the line of the error are provided in the error message.

## Parsing the number

`def parse_number(line: str) -> str`

Checking for and returning an integer.

**Example:**

```
315
```

## Parsing the time

`def parse_time(line: str) -> str`

Checking for a valid line with times. Returning only the hours, minutes, and seconds of the starting time.

**Example:**

```
00:02:22,000 --> 00:02:27,000
```

returns: `00:02:22`

## Parsing the message

`parse_message(line: str) -> List[str]`

Extracting the chatter and the message:
- The chatter and the message are divided by the first `:`.
- The chatter may be prefixed with a `@` which must be ignored.
- The message can be empty.

**Example:**

```
Kali Co: EEEEEP!!! so excited for this!!! ❤️
```

returns: `["Kali Co", "EEEEEP!!! so excited for this!!!"]`.

## Ranking

`def get_rank(chats: List[Dict], field: str, top_n: int = None) -> List[Tuple[str, int]]`

- Ranking the chatters and the streams by the number of chats.
- Ranking the words by the number of times they occur.
- Words get only counted if they are not in the list of stopwords and if they are at least 3 characters long.

The `field` parameter is for choosing the ranking of words, chatters, or chats.

The `top_n` parameter limits the result to n rankings.

## Format the ranking

```
def format_rank(
    ranks: List[Tuple[str, int]],
    column1: str = "Rank",
    column2: str = "Value",
    column3: str = "#",
) -> List[Dict]:
```

The ranking gets formatted into a dictionary with 3 columns.

## Writing the chats into a `.csv` File

`def write_csv(dir: str, file_name: str, chats: List[Dict]) -> None`

All chats get written into a `.csv` File.

## Writing the wordcloud

`def write_wordcloud(dir: str, file_name: str, words: List[Tuple[str, int]]) -> None:`

Creating the wordcloud image.
