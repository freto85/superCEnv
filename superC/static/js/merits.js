
function medalCalculation() {
  var medalNumber = [0,0,0,0,0,0]
  for (i = 0; i < medals.length; i++) {
     if (medals[i] >= 100) {
       medalNumber[1]++
    }
    if (medals[i] >= 250) {
       medalNumber[2]++
    }
    if (medals[i] >= 500) {
       medalNumber[3]++
    }
    if (medals[i] >= 800) {
       medalNumber[4]++
    }
    if (medals[i] >= 1200) {
       medalNumber[5]++
    }
    if (medalNumber[i] < 100) {
      medalNumber[0] ++
    }
  }

  return medalNumber
}


function calculateTrophies() {
    var numberOfTrophies = 0;

    if (trophies[0] >= 5) {
      numberOfTrophies++
    }
    if (trophies[0] >= 10) {
      numberOfTrophies++
    }
    if  ( trophies[0] >= 20) {
      numberOfTrophies++
    }
    if (trophies[1] >= 1) {
      numberOfTrophies++
    }
    if (trophies[1] >= 5) {
      numberOfTrophies++
    }
    if (trophies[2] >= 1) {
      numberOfTrophies++
    }
    if (trophies[2] >= 5) {
      numberOfTrophies++
    }
    if (trophies[2] >= 8) {
      numberOfTrophies++
    }
    if (trophies[3] >= 1) {
      numberOfTrophies++
    }
    if (trophies[3] >= 3) {
      numberOfTrophies++
    }
    if (trophies[4] >= 20) {
      numberOfTrophies++
    }
    if (trophies[4] >= 50) {
      numberOfTrophies++
    }
    if (trophies[4] >= 100) {
      numberOfTrophies++
    }
    if (trophies[4] >= 200) {
      numberOfTrophies++
    }
    if (trophies[5] >= 50) {
      numberOfTrophies++
    }
    if (trophies[6] >= 5) {
      numberOfTrophies++
    }
    if (trophies[6] >= 12) {
      numberOfTrophies++
    }
    if (trophies[6] >= 20) {
      numberOfTrophies++
    }
    if (trophies[7] >= 5) {
      numberOfTrophies++
    }
    if (trophies[7] >= 10) {
      numberOfTrophies++
    }
    if (trophies[8] >= 3) {
      numberOfTrophies++
    }
    if (trophies[8] >= 10) {
      numberOfTrophies++
    }
    if (trophies[8] >= 20) {
      numberOfTrophies++
    }
    if (trophies[9] == 'True') {
      numberOfTrophies++
    }
    if (trophies[10] == 'True') {
      numberOfTrophies++
    }
    return numberOfTrophies
  }

function calculateStickers() {
  var numberOfStickers = 0
  for (i = 0;i < stickers.length; i++) {
    if (stickers[i] == 'True') {
      numberOfStickers++
    }
  }
  if (phonemesLearned >= 44) {
    numberOfStickers++
  }
  return numberOfStickers
}



var stickersTotal = calculateStickers()
var numberOfMedals = medalCalculation()
var trophiesTotal = calculateTrophies()
var selectSticker = document.getElementById('sticker-number')
selectSticker.innerText = stickersTotal
var selectTrophies = document.getElementById('trophy-number')
selectTrophies.innerText = trophiesTotal
var valuesOfMedals = [document.getElementById('bronze'),document.getElementById('silver'),document.getElementById('gold'),document.getElementById('platinum'),document.getElementById('diamond')]
valuesOfMedals[0].innerText = numberOfMedals[1]
valuesOfMedals[1].innerText = numberOfMedals[2]
valuesOfMedals[2].innerText = numberOfMedals[3]
valuesOfMedals[3].innerText = numberOfMedals[4]
valuesOfMedals[4].innerText = numberOfMedals[5]

var gameOfLife = document.getElementById('game-of-life')
var movieOne = document.getElementById('movie-1')
var heaveHo = document.getElementById('heave-ho')
var monopoly = document.getElementById('monopoly')
var darts = document.getElementById('dart-board')
var movieTwo = document.getElementById('movie-2')
var humanFallFlat = document.getElementById('human-fall-flat')
var cinema = document.getElementById('cinema')
var jenga = document.getElementById('jenga')
var movieThree = document.getElementById('movie-3')
var stickFight = document.getElementById('stick-fight')
var operation = document.getElementById('operation')
var movieFour = document.getElementById('movie-4')
var pikuniku = document.getElementById('pikuniku')
var keepTalking = document.getElementById('keep-talking')
var battleShip = document.getElementById('battleship')
var movieFive = document.getElementById('movie-5')
var loversDangerous = document.getElementById('lovers-dangerous')
var escapeRoom = document.getElementById('escape-room')
var chemistrySet = document.getElementById('chemistry-set')
var bakingTime = document.getElementById('baking-time')

if (trophiesTotal < 1) {

  gameOfLife.setAttribute('id','locked-one')
  gameOfLife.setAttribute('title','<strong>Locked</strong>')
  gameOfLife.setAttribute('data-content',"<strong>Requirements:</strong><li>1 Trophy.</li>")
}

if (trophiesTotal < 3 || numberOfMedals[1] < 2) {
  movieOne.setAttribute('id','locked-two')
  movieOne.setAttribute('title','<strong>Movie 1</strong>')
  movieOne.setAttribute('data-content',"<strong>Requirements:</strong><li>3 Trophies.</li><li>2 Bronze Medals</li>")
}

if (trophiesTotal < 3 || numberOfMedals[1] < 3 || roadmap[0] < 1) {
  if (gameOfLife.id == 'locked-one') {
    heaveHo.setAttribute('id','locked-three')
    heaveHo.setAttribute('title','<strong>Locked</strong>')
    heaveHo.setAttribute('data-content',"<strong>Requirements:</strong><li>[Secret Requirement]</li><li>3 Bronze Medals.</li><li>3 Trophies.</li>")}
  else {
    heaveHo.setAttribute('id','locked-three')
    heaveHo.setAttribute('title','<strong>Locked</strong>')
    heaveHo.setAttribute('data-content',"<strong>Requirements:</strong><li>Win 1 game of The Game of Life.</li><li>3 Bronze Medals.</li><li>3 Trophies.</li>")
  }
}

if (trophiesTotal < 3 || numberOfMedals[1] < 3 || stickersTotal < 1 || roadmap[2] < 2) {
  if (heaveHo.id == 'locked-three') {
    monopoly.setAttribute('id','locked-four')
    monopoly.setAttribute('title','<strong>Locked</strong>')
    monopoly.setAttribute('data-content',"<strong>Requirements:</strong><li>[Secret Requirement]</li><li>3 Bronze Medals.</li><li>3 Trophies.</li><li>1 Sticker.</li>")
  }
  else {
    monopoly.setAttribute('id','locked-four')
    monopoly.setAttribute('title','<strong>Locked</strong>')
    monopoly.setAttribute('data-content',"<strong>Requirements:</strong><li>Clear 2 Worlds at <strong>Heave Ho!</strong><li>3 Bronze Medals.</li><li>3 Trophies.</li><li>1 Sticker.</li>")
  }
}

if (trophiesTotal < 2 || numberOfMedals[1] < 3 || stickersTotal < 1 || roadmap[1] < 100) {
    darts.setAttribute('id','locked-five')
    darts.setAttribute('title','<strong>Locked</strong>')
    darts.setAttribute('data-content',"<strong>Requirements:</strong><li>Score 100 points at Scrabble.</li><li>3 Bronze Medals.</li><li>2 Trophies.</li><li>1 Sticker.</li>")
}

if (trophiesTotal < 5 || numberOfMedals[1] < 4 || stickersTotal < 2 || movieOne.id == 'locked-two' || stickers[5] == 'False') {
  if (movieOne.id == 'locked-two') {
    movieTwo.setAttribute('id','locked-six')
    movieTwo.setAttribute('title','<strong>Movie 2</strong>')
    movieTwo.setAttribute('data-content',"<strong>Requirements:</strong><li>Watch <strong>Movie 1</strong>.</li><li>4 Bronze Medals.</li><li>5 trophies.</li><li>2 Stickers.</li>")
  } else {
    movieTwo.setAttribute('id','locked-six')
    movieTwo.setAttribute('title','<strong>Movie 2</strong>')
    movieTwo.setAttribute('data-content',"<strong>Requirements:</strong><li>Watch <strong>The Secret Life of Walter Mitty</strong>.</li><li>4 Bronze Medals.</li><li>5 trophies.</li><li>2 Stickers.</li>")
  }
}

if (trophiesTotal < 5 || numberOfMedals[1] < 6 || stickersTotal < 2 || numberOfMedals[2] < 2 || heaveHo.id == 'locked-three') {
  if (heaveHo.id == 'locked-three') {
    humanFallFlat.setAttribute('id','locked-seven')
    humanFallFlat.setAttribute('title','<strong>Locked</strong>')
    humanFallFlat.setAttribute('data-content',"<strong>Requirements:</strong><li>Get every Bronze Medal.</li><li>2 Silver Medals.</li><li>5 trophies.</li><li>2 Stickers.</li><li>[Secret Requirement].</li>")
  } else {
    humanFallFlat.setAttribute('id','locked-seven')
    humanFallFlat.setAttribute('title','<strong>Locked</strong>')
    humanFallFlat.setAttribute('data-content',"<strong>Requirements:</strong><li>Get every Bronze Medal.</li><li>2 Silver Medals.</li><li>5 trophies. </li><li>2 Stickers.</li><li>Have <strong>Heave Ho!</strong> Unlocked!</li>")
  }
}

if (trophiesTotal < 5 || numberOfMedals[1] < 6 || stickersTotal < 2 || numberOfMedals[2] < 1 || roadmap[4] < 100) {
  if (darts.id == 'locked-five') {
    jenga.setAttribute('id','locked-eight')
    jenga.setAttribute('title','<strong>Locked</strong>')
    jenga.setAttribute('data-content',"<strong>Requirements:</strong><li>Get every Bronze Medal.</li><li>1 Silver Medal.</li><li>5 Trophies.</li><li>2 Stickers.</li><li>[Secret Requirement]</li>")
  } else {
    jenga.setAttribute('id','locked-eight')
    jenga.setAttribute('title','<strong>Locked</strong>')
    jenga.setAttribute('data-content',"<strong>Requirements:</strong><li>Get every Bronze Medal.</li><li>1 Silver Medal.</li><li>5 Trophies.</li><li>2 Stickers.</li><li>Score more than 100 points at Darts!</li>")
  }
}

if (numberOfMedals[2] < 3 || stickersTotal < 4 || roadmap[3] < 1 ||roadmap[5] < 1 || roadmap[6] < 3) {
  if (humanFallFlat.id == 'locked-seven' && jenga.id == 'locked-eight' && monopoly.id == 'locked-four') {
    cinema.setAttribute('id','locked-nine')
    cinema.setAttribute('title','<strong>Locked</strong>')
    cinema.setAttribute('data-content',"<strong>Requirements:</strong><li>3 Silver Medals.</li><li>4 Stickers.</li><li>[Secret Requirement]</li><li>[Secret Requirement]</li><li>[Secret Requirement]</li>")
  }
  else  if (humanFallFlat.id == 'locked-seven' && jenga.id == 'locked-eight' && monopoly.id == 'monopoly') {
    cinema.setAttribute('id','locked-nine')
    cinema.setAttribute('title','<strong>Locked</strong>')
    cinema.setAttribute('data-content',"<strong>Requirements:</strong><li>3 Silver Medals.</li><li>4 Stickers.</li><li>Win a game of <strong>Monopoly</strong></li><li>[Secret Requirement]</li><li>[Secret Requirement]</li>")
  }
  else if (humanFallFlat.id == 'human-fall-flat' && jenga.id == 'locked-eight' && monopoly.id == 'locked-four') {
    cinema.setAttribute('id','locked-nine')
    cinema.setAttribute('title','<strong>Locked</strong>')
    cinema.setAttribute('data-content',"<strong>Requirements:</strong><li>3 Silver Medals.</li><li>4 Stickers.</li><li>[Secret Requirement]</li><li>Clear a World at Human Fall Flat.</li><li>[Secret Requirement]</li>")
  }
  else if (humanFallFlat.id == 'locked-seven' && jenga.id == 'jenga' && monopoly.id == 'locked-four') {
    cinema.setAttribute('id','locked-nine')
    cinema.setAttribute('title','<strong>Locked</strong>')
    cinema.setAttribute('data-content',"<strong>Requirements:</strong><li>3 Silver Medals.</li><li>4 Stickers.</li><li>[Secret Requirement]</li><li>[Secret Requirement]</li><li>Win 3 Jenga matches.</li>")
  }
  else if (humanFallFlat.id == 'human-fall-flat' && jenga.id == 'jenga' && monopoly.id == 'locked-four') {
    cinema.setAttribute('id','locked-nine')
    cinema.setAttribute('title','<strong>Locked</strong>')
    cinema.setAttribute('data-content',"<strong>Requirements:</strong><li>3 Silver Medals.</li><li>4 Stickers.</li><li>[Secret Requirement]</li><li>Clear a World at Human Fall Flat.</li><li>Win 3 Jenga matches.</li>")
  }
  else if (humanFallFlat.id == 'locked-seven' && jenga.id == 'jenga' && monopoly.id == 'monopoly') {
    cinema.setAttribute('id','locked-nine')
    cinema.setAttribute('title','<strong>Locked</strong>')
    cinema.setAttribute('data-content',"<strong>Requirements:</strong><li>3 Silver Medals.</li><li>4 Stickers.</li><li>Win a game of <strong>Monopoly</strong></li><li>[Secret Requirement]</li><li>Win 3 Jenga matches.</li>")
}
  else if (humanFallFlat.id == 'human-fall-flat' && jenga.id == 'locked-eight' && monopoly.id == 'monopoly') {
    cinema.setAttribute('id','locked-nine')
    cinema.setAttribute('title','<strong>Locked</strong>')
    cinema.setAttribute('data-content',"<strong>Requirements:</strong><li>3 Silver Medals.</li><li>4 Stickers.</li><li>Win a game of <strong>Monopoly</strong></li><li>Clear a World at Human Fall Flat.</li><li>[Secret Requirement]</li>")
  }
  else {
    cinema.setAttribute('id','locked-nine')
    cinema.setAttribute('title','<strong>Locked</strong>')
    cinema.setAttribute('data-content',"<strong>Requirements:</strong><li>3 Silver Medals.</li><li>4 Stickers.</li><li>Win a game of <strong>Monopoly</strong></li><li>Clear a World at Human Fall Flat.</li><li>Win 3 Jenga matches.</li>")
  }
}

if (trophiesTotal < 8 || numberOfMedals[1] < 6 || stickersTotal < 4 || movieTwo.id == 'locked-six' || stickers[6] == 'False') {
  if (movieTwo.id == 'locked-six') {
    movieThree.setAttribute('id','locked-ten')
    movieThree.setAttribute('title','<strong>Movie 3</strong>')
    movieThree.setAttribute('data-content',"<strong>Requirements:</strong><li>Watch <strong>Movie 2</strong>.</li><li>Get every Bronze Medal.</li><li>8 trophies.</li><li>4 Stickers.</li>")
  } else {
    movieThree.setAttribute('id','locked-ten')
    movieThree.setAttribute('title','<strong>Movie 3</strong>')
    movieThree.setAttribute('data-content',"<strong>Requirements:</strong><li>Watch <strong>Big Fish</strong>.</li><li>Get every Bronze Medal.</li><li>8 trophies.</li><li>4 Stickers.</li>")
  }
}

if (trophiesTotal < 10 || numberOfMedals[2] < 6 || numberOfMedals[3] < 3 || stickersTotal < 5 || stickers[11] == "False") {
  if (cinema.id == 'locked-nine') {
    stickFight.setAttribute('id','locked-eleven')
    stickFight.setAttribute('title','<strong>Locked</strong>')
    stickFight.setAttribute('data-content',"<strong>Requirements:</strong><li>Get every Silver Medal.</li><li>3 Gold Medals.</li><li>9 Trophies.</li><li>5 Stickers.</li><li>[Secret Requirement]</li>")
  } else {
    stickFight.setAttribute('id','locked-eleven')
    stickFight.setAttribute('title','<strong>Locked</strong>')
    stickFight.setAttribute('data-content',"<strong>Requirements:</strong><li>Get every Silver Medal.</li><li>3 Gold Medals.</li><li>10 Trophies.</li><li>5 Stickers.</li><li>Complete the Cinema Event.</li>")
  }
}

if (trophiesTotal < 9 || numberOfMedals[2] < 6 || numberOfMedals[3] < 3 || stickersTotal < 6 || stickers[11] == "False") {
  if (cinema.id == 'locked-nine') {
    operation.setAttribute('id','locked-twelve')
    operation.setAttribute('title','<strong>Locked</strong>')
    operation.setAttribute('data-content',"<strong>Requirements:</strong><li>Get every Silver Medal.</li><li>2 Gold Medals.</li><li>9 Trophies.</li><li>6 Stickers.</li><li>[Secret Requirement]</li>")
  } else {
    operation.setAttribute('id','locked-twelve')
    operation.setAttribute('title','<strong>Locked</strong>')
    operation.setAttribute('data-content',"<strong>Requirements:</strong><li>Get every Silver Medal.</li><li>2 Gold Medals.</li><li>9 Trophies.</li><li>6 Stickers.</li><li>Complete the Cinema Event.</li>")
  }
}

if (trophiesTotal < 10 || numberOfMedals[2] < 6 || numberOfMedals[3] < 3 || stickersTotal < 6 || movieThree.id == 'locked-ten' || stickers[7] == "False") {
  if (movieThree.id == 'locked-ten') {
    movieFour.setAttribute('id','locked-thirteen')
    movieFour.setAttribute('title','<strong>Movie 4</strong>')
    movieFour.setAttribute('data-content',"<strong>Requirements:</strong><li>Watch <strong> Movie 3</strong>.</li><li>Get every Silver Medal.</li><li>3 Gold Medals.</li><li>10 Trophies.</li><li>6 Stickers.</li>")
  } else {
    movieFour.setAttribute('id','locked-thirteen')
    movieFour.setAttribute('title','<strong>Movie 4</strong>')
    movieFour.setAttribute('data-content',"<strong>Requirements:</strong><li>Watch <strong> Warm Bodies</strong>.</li><li>Get every Silver Medal.</li><li>3 Gold Medals.</li><li>10 Trophies.</li><li>6 Stickers.</li>")
  }
}

if (trophiesTotal < 12 || numberOfMedals[3] < 6 || numberOfMedals[4] < 1 || stickersTotal < 8 || roadmap[7] < 10) {
  if (stickFight.id == 'locked-eleven') {
    pikuniku.setAttribute('id','locked-fourteen')
    pikuniku.setAttribute('title','<strong>Locked</strong>')
    pikuniku.setAttribute('data-content',"<strong>Requirements:</strong><li>Get every Gold Medal.</li><li>1 Platinum Medal.</li><li>12 Trophies.</li><li>8 Stickers.</li><li>[Secret Requirement]</li>")
  } else {
    pikuniku.setAttribute('id','locked-fourteen')
    pikuniku.setAttribute('title','<strong>Locked</strong>')
    pikuniku.setAttribute('data-content',"<strong>Requirements:</strong><li>Get every Gold Medal.</li><li>1 Platinum Medal.</li><li>12 Trophies.</li><li>8 Stickers.</li><li>Win at Stick Fight 10 times!</li>")
  }
}

if (trophiesTotal < 13 || numberOfMedals[3] < 6 || numberOfMedals[4] < 2 || stickersTotal < 7 || roadmap[8] < 1) {
  if (operation.id == 'locked-twelve') {
    battleShip.setAttribute('id','locked-fifteen')
    battleShip.setAttribute('title','<strong>Locked</strong>')
    battleShip.setAttribute('data-content',"<strong>Requirements:</strong><li>Get every Gold Medal.</li><li>2 Platinum Medals.</li><li>13 Trophies.</li><li>7 Stickers.</li><li>[Secret Requirement]</li>")
  } else {
    battleShip.setAttribute('id','locked-fifteen')
    battleShip.setAttribute('title','<strong>Locked</strong>')
    battleShip.setAttribute('data-content',"<strong>Requirements:</strong><li>Get every Gold Medal.</li><li>2 Platinum Medals.</li><li>13 Trophies.</li><li>7 Stickers.</li><li>Win a game of Operation.</li>")
  }
}

if (trophiesTotal < 15 || numberOfMedals[4] < 3 || stickersTotal < 8 || roadmap[9] < 3 || roadmap[10] < 2 ) {
  if (pikuniku.id == 'locked-fourteen' && battleShip.id == 'locked-fifteen') {
    keepTalking.setAttribute('id','locked-sixteen')
    keepTalking.setAttribute('title','<strong>Locked</strong>')
    keepTalking.setAttribute('data-content',"<strong>Requirements:</strong><li>3 Platinum Medals.</li><li>15 Trophies.</li><li>8 Stickers.</li><li>[Secret Requirement]</li><li>[Secret Requirement]</li>")
  }
  if (pikuniku.id == 'locked-fourteen' && battleShip.id == 'battleship') {
    keepTalking.setAttribute('id','locked-sixteen')
    keepTalking.setAttribute('title','<strong>Locked</strong>')
    keepTalking.setAttribute('data-content',"<strong>Requirements:</strong><li>3 Platinum Medals.</li><li>15 Trophies.</li><li>8 Stickers.</li><li>[Secret Requirement]</li><li>Win 2 times at <strong>Battleship</strong>.</li>")
  }
  else if (battleShip.id == 'locked-fifteen' && pikuniku.id == 'pikuniku') {
    keepTalking.setAttribute('id','locked-sixteen')
    keepTalking.setAttribute('title','<strong>Locked</strong>')
    keepTalking.setAttribute('data-content',"<strong>Requirements:</strong><li>3 Platinum Medals.</li><li>15 Trophies.</li><li>8 Stickers.</li><li>Clear three levels of <strong>Pikuniku</strong></li><li>[Secret Requirement]</li>")
  }
  else {
    keepTalking.setAttribute('id','locked-sixteen')
    keepTalking.setAttribute('title','<strong>Locked</strong>')
    keepTalking.setAttribute('data-content',"<strong>Requirements:</strong><li>3 Platinum Medals.</li><li>15 Trophies.</li><li>8 Stickers.</li><li>Clear three levels of <strong>Pikuniku</strong>.</li><li>Win 2 times at <strong>Battleship</strong>.</li>")
  }
}

if (trophiesTotal < 15 || numberOfMedals[3] < 6 || numberOfMedals[4] < 4 || stickersTotal < 8 || movieFour.id == 'locked-thirteen') {
  if (movieFour.id == 'locked-thirteen') {
    movieFive.setAttribute('id','locked-seventeen')
    movieFive.setAttribute('title','<strong>Movie 5</strong>')
    movieFive.setAttribute('data-content',"<strong>Requirements:</strong><li>Watch <strong>Movie 4</strong></li><li>Get every Gold Medal</li><li>Get 4 Diamond Medals</li><li>15 Trophies</li><li>8 Stickers</li>")
  } else {
    movieFive.setAttribute('id','locked-seventeen')
    movieFive.setAttribute('title','<strong>Movie 5</strong>')
    movieFive.setAttribute('data-content',"<strong>Requirements:</strong><li>Watch <strong>The Help</strong></li><li>Get every Gold Medal</li><li>Get 4 Diamond Medals</li><li>15 Trophies</li><li>8 Stickers</li>")
  }
}

if (trophiesTotal < 18 || numberOfMedals[4] < 6 || numberOfMedals[5] < 2 || stickersTotal < 10 ||  roadmap[9] < 4) {
  if (pikuniku.id == 'locked-fourteen') {
    loversDangerous.setAttribute('id','locked-eighteen')
    loversDangerous.setAttribute('title','<strong>Locked</strong>')
    loversDangerous.setAttribute('data-content',"<strong>Requirements:</strong><li>Get every Diamond Medal.</li><li>2 Platinum Medals</li><li>18 Trophies</li><li>10 Stickers</li><li>[Secret Requirement]</li>")
    } else {
    loversDangerous.setAttribute('id','locked-eighteen')
    loversDangerous.setAttribute('title','<strong>Locked</strong>')
    loversDangerous.setAttribute('data-content',"<strong>Requirements:</strong><li>Get every Diamond Medal.</li><li>2 Platinum Medals</li><li>18 Trophies</li><li>10 Stickers</li><li>Clear 4 levels of <strong>Pikuniku</strong></li>")
  }
}

if (trophiesTotal < 16 || numberOfMedals[4] < 6 || numberOfMedals[5] < 2 || stickersTotal < 11 || roadmap[10] < 3) {
  if (battleShip.id == 'locked-fifteen') {
    chemistrySet.setAttribute('id','locked-nineteen')
    chemistrySet.setAttribute('title','<strong>Locked</strong>')
    chemistrySet.setAttribute('data-content',"<strong>Requirements:</strong><li>Get every Platinum Medal.</li><li>2 Diamond Medals</li><li>16 Trophies</li><li>11 Stickers</li><li>[Secret Requirement]")
    } else {
    chemistrySet.setAttribute('id','locked-nineteen')
    chemistrySet.setAttribute('title','<strong>Locked</strong>')
    chemistrySet.setAttribute('data-content',"<strong>Requirements:</strong><li>Get every Platinum Medal.</li><li>2 Diamond Medals</li><li>16 Trophies</li><li>11 Stickers</li><li> Win 3 times at <strong>Battleship</strong>")
  }
}

if (trophiesTotal < 20 || numberOfMedals[5] < 4 || stickersTotal < 12 || roadmap[12] == 'False' || roadmap[11] < 1 || roadmap[13] == 'False') {
  if (loversDangerous.id == 'locked-eighteen' && chemistrySet.id == 'locked-nineteen' && keepTalking.id == 'locked-sixteen') {
  escapeRoom.setAttribute('id','locked-twenty')
  escapeRoom.setAttribute('title','<strong>Locked</strong>')
  escapeRoom.setAttribute('data-content',"<strong>Requirements:</strong><li>4 Diamond Medals.</li><li>20 Trophies.</li><li>12 Stickers.</li><li>[Secret Requirement]</li><li>[Secret Requirement]</li><li>[Secret Requirement]</li>")
  }
  if (loversDangerous.id == 'locked-eighteen' && chemistrySet.id == 'chemistry-set' && keepTalking.id == 'keep-talking') {
    escapeRoom.setAttribute('id','locked-twenty')
    escapeRoom.setAttribute('title','<strong>Locked</strong>')
    escapeRoom.setAttribute('data-content',"<strong>Requirements:</strong><li>4 Diamond Medals</li><li>20 Trophies</li><li>12 Stickers</li><li>Succesfully defuse a bomb.</li><li>[Secret Requirement]</li><li>Succesfully perform a Chemistry Experiment</li>")
  }
  else if (loversDangerous.id == 'lovers-dangerous' && pikuniku.id == 'locked-nineteen' && keepTalking.id == 'keep-talking') {
    escapeRoom.setAttribute('id','locked-twenty')
    escapeRoom.setAttribute('title','<strong>Locked</strong>')
    escapeRoom.setAttribute('data-content',"<strong>Requirements:</strong><li>4 Diamond Medals</li><li>20 Trophies</li><li>12 Stickers</li><li>Succesfully defuse a bomb.</li><li>Complete a Level in <strong>Lovers in a Dangerous Spacetime</strong></li><li>[Secret Requirement]</li>")
  }
  else if (loversDangerous.id == 'lovers-dangerous' && pikuniku.id == 'chemistry-set' && keepTalking.id == 'locked-sixteen') {
    escapeRoom.setAttribute('id','locked-twenty')
    escapeRoom.setAttribute('title','<strong>Locked</strong>')
    escapeRoom.setAttribute('data-content',"<strong>Requirements:</strong><li>4 Diamond Medals</li><li>20 Trophies</li><li>12 Stickers</li><li>[Secret Requirement]</li><li>Complete a Level in <strong>Lovers in a Dangerous Spacetime</strong></li><li>Succesfully perform a Chemistry Experiment</li>")
  }
  else if (loversDangerous.id == 'locked-eighteen' && chemistrySet.id == 'locked-nineteen' && keepTalking.id == 'keep-talking') {
    escapeRoom.setAttribute('id','locked-twenty')
    escapeRoom.setAttribute('title','<strong>Locked</strong>')
    escapeRoom.setAttribute('data-content',"<strong>Requirements:</strong><li>4 Diamond Medals</li><li>20 Trophies</li><li>12 Stickers</li><li>Succesfully defuse a bomb.</li><li>[Secret Requirement]</li><li>[Secret Requirement]</li>")
  }
  else if (loversDangerous.id == 'lovers-dangerous' && chemistrySet.id == 'locked-nineteen' && keepTalking.id == 'locked-sixteen') {
    escapeRoom.setAttribute('id','locked-twenty')
    escapeRoom.setAttribute('title','<strong>Locked</strong>')
    escapeRoom.setAttribute('data-content',"<strong>Requirements:</strong><li>4 Diamond Medals</li><li>20 Trophies</li><li>12 Stickers</li><li>[Secret Requirement]</li><li>Complete a Level in <strong>Lovers in a Dangerous Spacetime</strong></li><li>[Secret Requirement]</li>")
  }
  else if (loversDangerous.id == 'locked-eighteen' && chemistrySet.id == 'chemistry-set' && keepTalking.id == 'locked-sixteen') {
    escapeRoom.setAttribute('id','locked-twenty')
    escapeRoom.setAttribute('title','<strong>Locked</strong>')
    escapeRoom.setAttribute('data-content',"<strong>Requirements:</strong><li>4 Diamond Medals</li><li>20 Trophies</li><li>12 Stickers</li><li>[Secret Requirement]</li><li>[Secret Requirement]</li><li>Succesfully perform a <strong>Chemistry Experiment</strong>.</li>")
  }

  else {
    escapeRoom.setAttribute('id','locked-twenty')
    escapeRoom.setAttribute('title','<strong>Locked</strong>')
    escapeRoom.setAttribute('data-content',"<strong>Requirements:</strong><li>4 Diamond Medals.</li><li>20 Trophies.</li><li>12 Stickers.</li><li>Succesfully defuse a bomb.</li><li>Complete a Level in <strong>L.I.A.D.S.T.</strong></li><li>Succesfully perform a <strong>Chemistry Experiment</strong></li>")
  }

}

if (trophiesTotal < 18 || numberOfMedals[4] < 6 || numberOfMedals[5] < 3 || stickersTotal < 10 || movieFive.id == 'locked-seventeen') {
  if (movieFive.id == 'locked-seventeen') {
    bakingTime.setAttribute('id','locked-twenty-one')
    bakingTime.setAttribute('title','<strong>Locked</strong>')
    bakingTime.setAttribute('data-content',"<strong>Requirements:</strong><li>Watch <strong>Movie 5</strong></li><li>Get every Platinum Medal</li><li>Get 3 Diamond Medals</li><li>15 Trophies</li><li>8 Stickers</li>")
  } else {
    bakingTime.setAttribute('id','locked-twenty-one')
    bakingTime.setAttribute('title','<strong>Baking Time!</strong>')
    bakingTime.setAttribute('data-content',"<strong>Requirements:</strong><li>Watch <strong>Reign Over Me</strong></li><li>Get every Platinum Medal.</li><li>Get 3 Diamond Medals.</li><li>18 Trophies</li><li>10 Stickers</li>")
  }
}
