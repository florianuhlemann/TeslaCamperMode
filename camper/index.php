<!DOCTYPE html>
<html>
<head>
    <title>Tesla Camper Mode v0.1.0</title>
    <link rel="stylesheet" type="text/css" href="css/style.css">
</head>
<body>
<div class="container">
	<h1 class="center">Tesla Camper Mode v0.1.0</h1>
    <?php
        if (file_exists("is_currently_heating")) {
            echo '<h4 class="center subtitle">Your vehicle is currently heating...</h4>';
        } else {
            //echo "Not logging...";
        }
    ?>
</div>
<?php if(!file_exists("is_currently_heating")): ?>
	<button class="left-button" onclick="requestPassword()">START</button>
    <script src="js/jquery.min.js"></script>
	<script type="text/javascript">
		function requestPassword() {
		    var password = prompt("Password");
		    $.ajax({
		        data: 'password=' + password + '&command=start',
		        url: 'command.php',
		        method: 'POST', // or GET
		        success: function(msg) {}
		    });
		    window.setTimeout('location.reload()', 500);
		}
	</script>
<?php elseif(file_exists("is_currently_heating")): ?>
		<button class="right-button" onclick="requestPassword()">STOP</button>
	    <script src="js/jquery.min.js"></script>
		<script type="text/javascript">
			function requestPassword() {
			    var password = prompt("Password");
			    $.ajax({
			        data: 'password=' + password + '&command=stop',
			        url: 'command.php',
			        method: 'POST', // or GET
			        success: function(msg) {}
			    });
			    window.setTimeout('location.reload()', 500);
			}
		</script>
<?php endif; ?>
</body>
</html>