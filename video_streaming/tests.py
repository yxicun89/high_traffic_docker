from django.test import TestCase
from django.urls import reverse

class VideoStreamingViewTests(TestCase):
    def test_video_streaming_home_view(self):
        response = self.client.get(reverse('video_streaming_home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Video Streaming Home")

    def test_video_streaming_view_template(self):
        response = self.client.get(reverse('video_streaming_home'))
        self.assertTemplateUsed(response, 'video_streaming/home.html')  # Adjust template name as necessary

    # Add more tests as needed for additional functionality in the video streaming application.