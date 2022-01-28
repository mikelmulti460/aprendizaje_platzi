function Car(licence, driver){
    this.id;
    this.licence = licence;
    this.driver = driver;
    this.passenger;
    
}

Car.prototype.printDataCar = function(){
    console.log(this.driver)
    console.log(this.driver.name)
    console.log(this.driver.document)
    console.log("Licencia: "+this.licence)
}