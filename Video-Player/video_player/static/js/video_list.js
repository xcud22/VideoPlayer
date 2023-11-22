let videoContainer=document.getElementById('videoContainer');
let videoUrls=videoContainer.getAttribute('data-videourls').split(',');
console.log(videoUrls);
let videoPlayer=document.getElementById('videoPlayer');
let playButton=document.getElementById('playButton');
let currentVideoIndex=0;

playButton.addEventListener('click', function() {
        videoPlayer.src=videoUrls[currentVideoIndex];
        videoPlayer.play();
        videoContainer.requestFullscreen();
    });

videoPlayer.addEventListener('ended', function() {
        currentVideoIndex++;

        if(currentVideoIndex >=videoUrls.length) {
            currentVideoIndex=0;
        }

        videoPlayer.src=videoUrls[currentVideoIndex];
        videoPlayer.play();
    });