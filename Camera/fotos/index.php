<!DOCTYPE html>
<html>
<head>
    <style>
        .foto {
            width: 100%;
        }
    </style>
    <title>Robowilly Fotos</title>
</head>
<body>
<span id="time-stamp"></span>
<img class='foto' src='shoot_and_show.gif' id="myImage" alt="If you see this message probably the robot stop broadcasting">
<script>
    setInterval(function() {
        let timeStampElement = document.getElementById('time-stamp');
        let myImageElement = document.getElementById('myImage');
        let timeStamp = Math.floor(Date.now() / 1000);
        timeStampElement.innerHTML = timeStamp.toString();
        myImageElement.src = 'shoot_and_show.gif?rand=' + timeStamp;
    }, 5000);
</script>
</body>
</html>

