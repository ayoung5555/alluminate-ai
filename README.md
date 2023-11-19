# Alluminate API Documentation

API code located in `src/backend/`

## get-video

Call to be made when user submits query from search box. Returns all information needed to render the right-hand side of the UI, including the top 5 videos, titles, authors, and other basic information.

- **Method:** POST
- **Endpoint:** `/get-video/`
- **Send Body:**
    ```json
    {
        "user_message": "how to code a binary tree"
    }
    ```
- **Example Return Body:** [return.json](https://github.com/ayoung5555/alluminate-ai/blob/main/src/backend/get-video/return.json)


## get-timestamps

Once get-video returns with the list of video ids, call get-timestamps on the current video being shown to user. It will take about 5-7 seconds to generate timestamps and relevant section titles, regardless of if the video has chapters or not.

- **Method:** GET
- **Endpoint:** `/get-timestamps/`
- **Send Body:**
    ```json
    {
      "video_id": "-9CLMxYf2MI"
    }
    ```
- **Example Return Body:** [return.json](https://github.com/ayoung5555/alluminate-ai/blob/main/src/backend/get-timestamps/return.json)


# Condensed Prototype Demos


## Figma Prototype



## Browser Prototpe without APIs



