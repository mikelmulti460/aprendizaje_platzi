<?php
    require_once("car.php");
    require_once("uberX.php");
    require_once("account.php");
    require_once("uberPool.php");

    $uberX = new UberX("MIJ341", new Account("Mikel Aranda", "JHF175"), "Chevrolet", "Spark");
    $uberX->printDataCar();
    echo "<br>";
    $uberPool = new UberPool("MIJ7841", new Account("Mikel Vieira", "JHF775"), "Toyota", "SpaYaris");
    $uberPool->printDataCar();
?>