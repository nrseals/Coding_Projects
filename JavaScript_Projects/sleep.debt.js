const getSleepHours = day => {
    switch (day) {
      case 'monday':
        return 8;
        break;
      case 'tuesday':
        return 7;
        break;
      case 'wednesday':
        return 8;
        break;
      case 'thursday':
        return 6;
        break;
      case 'friday':
        return 6;
        break;
      case 'saturday':
        return 7;
        break;
      case 'sunday':
        return 8;
        break;
      default:
        console.log('Error')
        break;
    }
  }
  
  //tests for getSleepHours
  // console.log(getSleepHours('monday'))
  // console.log(getSleepHours('tuesday'))
  
  const getActualSleepHours = () => {
    let monday = getSleepHours('monday')
    let tuesday = getSleepHours('tuesday')
    let wednesday = getSleepHours('wednesday')
    let thursday = getSleepHours('thursday')
    let friday = getSleepHours('friday')
    let saturday = getSleepHours('saturday')
    let sunday = getSleepHours('sunday')
    let sum = monday + tuesday + wednesday + thursday + friday + saturday + sunday;
    return sum; //no implicit return
  }
  //test for getActual
  // console.log(getActualSleepHours())
  
  const getIdealSleepHours = num => {
    let idealHours = num;
    return idealHours * 7;
  }
  //test for Ideal
  // console.log(getIdealSleepHours())
  const calculateSleepDebt = () => {
    let actualSleepHours = getActualSleepHours();
    let idealSleepHours = getIdealSleepHours(8);
    if (actualSleepHours === idealSleepHours){
      console.log("Sleep goal met")
    }
    if (actualSleepHours > idealSleepHours){
      let over = actualSleepHours - idealSleepHours
      console.log(`Overslept by ${over} hours`)
    }
    if (actualSleepHours < idealSleepHours){
      let under = idealSleepHours - actualSleepHours
      console.log(`Sleep deprived by ${under} hours. Get some rest`)
    }
  }
  calculateSleepDebt();