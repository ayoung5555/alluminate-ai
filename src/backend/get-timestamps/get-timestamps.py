from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter

import json
from openai import AzureOpenAI

prompt = ''

client = AzureOpenAI(
    azure_endpoint = "FIXME",
    api_key = "FIXME",
    api_version = "FIXME"
)


def get_timestamps(video_id):
    original_return_body =  YouTubeTranscriptApi.get_transcript(video_id)
    # print(original_return_body)
    # original_return_body = transcript_api_response
    # print(original_return_body)
    formatter = JSONFormatter()
    print("got transcript") # TODO: remove this
    complete_transcript = ' '.join([i["text"] for i in original_return_body])
    complete_transcript = complete_transcript.replace("\"", "")
    complete_transcript = complete_transcript.replace("\xa0", "")
    
    return_body = formatter.format_transcript(original_return_body)
    return_body = return_body.replace("\xa0", "")
    return_body = json.loads(return_body)

    json_string = get_important_sections(complete_transcript)


    try:
        json_array = json.loads(json_string)
    except Exception as e:
        print(e)
        print("get_timestamps error")
        return "error"
    # once we have the json array, iterate through each object in the array
    # and append the timestamp from the start of the section_transcript
    # to the object
    # then return the array
    print("searching...")
    for chapter in json_array:
        ts = timestamp_search(chapter["first_six"], return_body)
        chapter["timestamp"] = ts
    print("search complete")
    return json_array

# efficiently searches for the timestamp of the first occurence of the first_six words in the transcript
# searches TS 1, TS 2, TS 1+2, TS 3, TS 2+3, TS 4, TS 3+4...
def timestamp_search(first_six, return_body):
    # iterate through all the keys in the json body and 
    # return_body is a list of json objections or dictionaries
    # print ("First six: %s" % first_six)
    for index, line in enumerate(return_body):
        # print("line: %s" % line)
        # print("index: %s" % index)
        # print("line[text]: %s" % line["text"])
        line["text"] = line["text"].replace("\xa0", "")
        first_six = first_six.replace("\xa0", "")
        if index >= 0:
            # normal case
            if first_six in str(line["text"]):
                return line["start"]
            if first_six in (str(return_body[index - 1]["text"] + " " + line["text"])):
                return return_body[index-1]["start"]
        elif index == 0:
            # first line edge case
            if first_six in str(line["text"]):
                return line["start"]
        else:
            print("No match found for first_six: %s" % first_six)
            return -2
    print("Empty transcript")
    return -1
        

def get_important_sections(complete_transcript):
    # return the 5 most important parts of the video by analysing the transcript
    # call chatGPT to return an array of 5 json objects
    # {id, section_summary_title, section_transcript}
    # then use python to clean up any text surrounding the json array (maybe through regex?)
    # and return the json array
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "user", 
                 "content": "%s \nTranscript: %s" % (prompt, complete_transcript)},
            ]
        )
    
        return response.choices[0].message.content

    except Exception as e:
        # Handles all other exceptions
        print("An exception has occured. {}".format(e))
        return "error"



def main():
    # video_id = "JGLfyTDgfDc"
    print(get_timestamps(video_id))


if __name__ == "__main__":
    main()
