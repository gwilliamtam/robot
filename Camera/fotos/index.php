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
<img class='foto' src='shoot_and_show.gif' id="myImage">
<script>
    setInterval(function() {
        var myImageElement = document.getElementById('myImage');
        myImageElement.src = 'shoot_and_show.gif?rand=' + Math.random();
    }, 5000);
</script>
</body>
</html>

