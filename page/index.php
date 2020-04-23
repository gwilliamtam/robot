<h1>Test running python commands from php</h1>
<a href="index.php?command=l">Lights<a>
<?php
if (!empty($_GET)) {}
system("python3 test.py");

