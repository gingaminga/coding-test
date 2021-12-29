function solution(s) {
  let answer = s;
  const enNumbers = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
  ];

  enNumbers.map((enNum, i) => {
    const regexp = new RegExp(enNum, "g");
    answer = answer.replace(regexp, i);
  });

  return Number(answer);
}

solution("one4seveneight"); // 1478
solution("23four5six7"); // 234567
solution("2three45sixseven"); // 234567
solution("123"); // 123

// https://programmers.co.kr/learn/courses/30/lessons/81301
