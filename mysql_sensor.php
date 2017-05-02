<html>
<head>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js" type="text/javascript"></script>
<script src="http://maps.googleapis.com/maps/api/js"></script>



<style type="text/css">
  
td {
  height: 70px;
}

</style>

<?php
    echo 'starting again'."\r\n"; 
    $link = mysql_connect('localhost', 'root', 'root');
    if(!$link) 
    {
    	die('Could not connect: ' . mysql_error());
    }
   
    echo 'Connected successfully'."\r\n"; 
   
    $db_selected = mysql_select_db('sensor',$link);
	if(!$db_selected)
	{	 
    		die('Could not select database');
	}

  // Performing SQL query
  //$query = "SELECT  FROM sensorData";
  $query = "SELECT lat, lon, temperature, datetime FROM sensorData WHERE id=(SELECT MAX(id) FROM sensorData) limit 1";
        
  $result = mysql_query($query) or die('Query failed: ' . mysql_error());
  // Printing results in HTML
  $line = mysql_fetch_array($result);
   
  print_r($line);  

  $latlonString = $line["lat"].','.$line["lon"];
    mysql_close($conn);
?>

<script>
function initialize() 
{
	var mapProp = {
		center:new google.maps.LatLng(<?php echo $latlonString; ?>),
    		zoom:14,
    		mapTypeId:google.maps.MapTypeId.ROADMAP
  		};
  
	var map=new google.maps.Map(document.getElementById("googleMap"),mapProp);
  var myLatLng = {lat: <?php echo $line["lat"]; ?>, lng: <?php echo $line["lon"]; ?>};

   var marker = new google.maps.Marker({
    position: myLatLng,
    map: map,
    title: 'Current Location'
  });
}

// auto refresh

setInterval(function(){
   $('my_div').load('/var/www/html/mysql_sensor.php');
}, 2000) /* time in milliseconds (ie 2 seconds)*/


google.maps.event.addDomListener(window, 'load', initialize);
</script>
</head>
<body>
<div id="googleMap" style="width:50%;height:100%;float:right;"></div>
<div >
<h1 align="center" style="color : blue" >GPS Tracking</h1>
<table  style="font-size:30px;text-align:left;" width="50%" align="left">
   
    <tr>
      <td><div id = "my_div">Temprature</td><td><?php echo $line["temperature"]; ?></div></td>
      
    </tr>
    <tr>
      <td><div id = "my_div">Light</td><td><?php echo $line["lightPercentValue"]; ?></div></td>
      
    </tr>
    <tr>
      <td><div id = "my_div">Lattitude</td><td><?php echo $line["lat"]; ?></div></td>
      
    </tr>
    <tr>
      <td><div id = "my_div">Longitude</td><td><?php echo $line["lon"]; ?></div></td>      
    </tr>
    <tr>
      <td><div id = "my_div">Date Time</td><td><?php echo $line["datetime"]; ?></div></td>      
    </tr>

</table>
</div>
</body>
</html>
