function solution(lottos, win_nums) {
  const answer = [];

  const count = lottos.filter((values) => win_nums.includes(values)).length;
  const zeroCount = lottos.filter((values) => values === 0).length;

  const highLevel = 7 - (count + zeroCount) > 6 ? 6 : 7 - (count + zeroCount);
  const lowLevel = count < 2 ? 6 : 7 - count;

  answer.push(highLevel, lowLevel);

  console.log(answer);

  return answer;
}

solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]); // [3, 5]
solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]); // [1, 6]
solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]); // [1, 1]

// https://programmers.co.kr/learn/courses/30/lessons/77484
