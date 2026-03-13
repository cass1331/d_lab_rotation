import deeplabcut
deeplabcut.create_new_project(
    "test_project",
    "Jocasta",
    [r"Z:\users\mengyul\NPX\npx5\behavior\behavior_videos_mp4\npx5_20260312_s4_headfixed_03-12-26_14-13-31.mp4",
     r"Z:\users\mengyul\NPX\npx5\behavior\behavior_videos_mp4\npx5_20260312_s3_headfixed_03-12-26_14-00-23.mp4", 
     r"Z:\users\mengyul\NPX\npx5\behavior\behavior_videos_mp4\npx5_20260312_s1_headfixed_03-12-26_13-34-44.mp4"],
    working_directory=r"C:\Users\dlab\Documents\Mengyu\video_analysis\video_data",
    copy_videos=False,
    multianimal=False
)

#note to sekf: don't write images to the repo folder