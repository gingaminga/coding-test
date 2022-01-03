function solution(a, b) {
  const weekend = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"];
  const day = new Date(`2016-${a}-${b}`).getDay();

  return weekend[day];
}

solution(5, 24); // TUE

// https://programmers.co.kr/learn/courses/30/lessons/12901?language=javascript
