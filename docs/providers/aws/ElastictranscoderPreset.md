# Terraform::AWS::ElastictranscoderPreset

Provides an Elastic Transcoder preset resource.

## Properties

`Audio` - (Optional, Forces new resource) Audio parameters object (documented below).

`AudioCodecOptions` - (Optional, Forces new resource) Codec options for the audio parameters (documented below).

`Container` - (Required, Forces new resource) The container type for the output file. Valid values are `flac`, `flv`, `fmp4`, `gif`, `mp3`, `mp4`, `mpg`, `mxf`, `oga`, `ogg`, `ts`, and `webm`.

`Description` - (Optional, Forces new resource) A description of the preset (maximum 255 characters).

`Name` - (Optional, Forces new resource) The name of the preset. (maximum 40 characters).

`Thumbnails` - (Optional, Forces new resource) Thumbnail parameters object (documented below).

`Video` - (Optional, Forces new resource) Video parameters object (documented below).

`VideoWatermarks` - (Optional, Forces new resource) Watermark parameters for the video parameters (documented below).

`AudioPackingMode` - The method of organizing audio channels and tracks. Use Audio:Channels to specify the number of channels in your output, and Audio:AudioPackingMode to specify the number of tracks and their relation to the channels. If you do not specify an Audio:AudioPackingMode, Elastic Transcoder uses SingleTrack.

`BitRate` - The bit rate of the video stream in the output file, in kilobits/second. You can configure variable bit rate or constant bit rate encoding.

`Channels` - The number of audio channels in the output file.

`Codec` - The video codec for the output file. Valid values are `gif`, `H.264`, `mpeg2`, `vp8`, and `vp9`.

`SampleRate` - The sample rate of the audio stream in the output file, in hertz. Valid values are: `auto`, `22050`, `32000`, `44100`, `48000`, `96000`.

`BitDepth` - The bit depth of a sample is how many bits of information are included in the audio samples. Valid values are `16` and `24`. (FLAC/PCM Only).

`BitOrder` - The order the bits of a PCM sample are stored in. The supported value is LittleEndian. (PCM Only).

`Profile` - If you specified AAC for Audio:Codec, choose the AAC profile for the output file.

`Signed` - Whether audio samples are represented with negative and positive numbers (signed) or only positive numbers (unsigned). The supported value is Signed. (PCM Only).

`AspectRatio` - The display aspect ratio of the video in the output file. Valid values are: `auto`, `1:1`, `4:3`, `3:2`, `16:9`. (Note; to better control resolution and aspect ratio of output videos, we recommend that you use the values `MaxWidth`, `MaxHeight`, `SizingPolicy`, `PaddingPolicy`, and `DisplayAspectRatio` instead of `Resolution` and `AspectRatio`.).

`Format` - The format of thumbnails, if any. Valid formats are jpg and png.

`Interval` - The approximate number of seconds between thumbnails. The value must be an integer. The actual interval can vary by several seconds from one thumbnail to the next.

`MaxHeight` - The maximum height of the watermark.

`MaxWidth` - The maximum width of the watermark.

`PaddingPolicy` - When you set PaddingPolicy to Pad, Elastic Transcoder might add black bars to the top and bottom and/or left and right sides of the output video to make the total size of the output video match the values that you specified for `MaxWidth` and `MaxHeight`.

`Resolution` - The width and height of the video in the output file, in pixels. Valid values are `auto` and `widthxheight`. (see note for `AspectRatio`).

`SizingPolicy` - A value that controls scaling of the watermark. Valid values are: `Fit`, `Stretch`, `ShrinkToFit`.

`DisplayAspectRatio` - The value that Elastic Transcoder adds to the metadata in the output file. If you set DisplayAspectRatio to auto, Elastic Transcoder chooses an aspect ratio that ensures square pixels. If you specify another option, Elastic Transcoder sets that value in the output file.

`FixedGop` - Whether to use a fixed value for Video:FixedGOP. Not applicable for containers of type gif. Valid values are true and false. Also known as, Fixed Number of Frames Between Keyframes.

`FrameRate` - The frames per second for the video stream in the output file. The following values are valid: `auto`, `10`, `15`, `23.97`, `24`, `25`, `29.97`, `30`, `50`, `60`.

`KeyframesMaxDist` - The maximum number of frames between key frames. Not applicable for containers of type gif.

`MaxFrameRate` - If you specify auto for FrameRate, Elastic Transcoder uses the frame rate of the input video for the frame rate of the output video, up to the maximum frame rate. If you do not specify a MaxFrameRate, Elastic Transcoder will use a default of 30.

`HorizontalAlign` - The horizontal position of the watermark unless you specify a nonzero value for `horzontal_offset`.

`HorizontalOffset` - The amount by which you want the horizontal position of the watermark to be offset from the position specified by `HorizontalAlign`.

`Id` - A unique identifier for the settings for one watermark. The value of Id can be up to 40 characters long. You can specify settings for up to four watermarks.

`Opacity` - A percentage that indicates how much you want a watermark to obscure the video in the location where it appears.

`Target` - A value that determines how Elastic Transcoder interprets values that you specified for `video_watermarks.horizontal_offset`, `video_watermarks.vertical_offset`, `video_watermarks.max_width`, and `video_watermarks.max_height`. Valid values are `Content` and `Frame`.

`VerticalAlign` - The vertical position of the watermark unless you specify a nonzero value for `VerticalAlign`. Valid values are `Top`, `Bottom`, `Center`.

`VerticalOffset` - The amount by which you want the vertical position of the watermark to be offset from the position specified by `VerticalAlign`.

`Profile` - The codec profile that you want to use for the output file. (H.264/VP8 Only).

`Level` - The H.264 level that you want to use for the output file. Elastic Transcoder supports the following levels: `1`, `1b`, `1.1`, `1.2`, `1.3`, `2`, `2.1`, `2.2`, `3`, `3.1`, `3.2`, `4`, `4.1` (H.264 only).

`MaxReferenceFrames` - The maximum number of previously decoded frames to use as a reference for decoding future frames. Valid values are integers 0 through 16. (H.264 only).

`MaxBitRate` - The maximum number of kilobits per second in the output video. Specify a value between 16 and 62,500 inclusive, or `auto`. (Optional, H.264/MPEG2/VP8/VP9 only).

`BufferSize` - The maximum number of kilobits in any x seconds of the output video. This window is commonly 10 seconds, the standard segment duration when you're using ts for the container type of the output video. Specify an integer greater than 0. If you specify MaxBitRate and omit BufferSize, Elastic Transcoder sets BufferSize to 10 times the value of MaxBitRate. (Optional, H.264/MPEG2/VP8/VP9 only).

`InterlacedMode` -  The interlace mode for the output video. (Optional, H.264/MPEG2 Only).

`ColorSpaceConversion` - The color space conversion Elastic Transcoder applies to the output video. Valid values are `None`, `Bt709toBt601`, `Bt601toBt709`, and `Auto`. (Optional, H.264/MPEG2 Only).

`ChromaSubsampling` - The sampling pattern for the chroma (color) channels of the output video. Valid values are `yuv420p` and `yuv422p`.

`LoopCount` - The number of times you want the output gif to loop (Gif only).


## See Also

* [aws_elastictranscoder_preset](https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset.html) in the _Terraform Provider Documentation_