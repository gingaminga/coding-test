function solution(new_id) {
  let answer = new_id;

  // 1단계
  answer = answer.toLowerCase();
  console.log(answer);

  // 2단계
  let reg = /[^a-z0-9-_.]/g;
  answer = answer.replace(reg, "");
  console.log(answer);

  // 3단계
  reg = /[.+]+/g;
  answer = answer.replace(reg, ".");
  console.log(answer);

  // 4단계
  reg = /^[.]|[.]$/g;
  answer = answer.replace(reg, "");
  console.log(answer);

  // 5단계
  answer = answer.replace(/\s/, "");
  if (!answer) answer = "a";
  console.log(answer);

  // 6단계
  if (answer.length >= 16) {
    answer = answer.substr(0, 15);

    reg = /[.]$/g;
    answer = answer.replace(reg, "");
  }
  console.log(answer);

  // 7단계
  if (answer.length <= 2) {
    const finalText = answer.substr(-1);

    const answerLen = answer.length;

    for (let i = 0; i < 3 - answerLen; i++) {
      answer += finalText;
    }
  }
  console.log(answer);

  return answer;
}

solution("...!@BaT#*..y.abcdefghijklm"); // bat.y.abcdefghi
solution("z-+.^."); // z--
solution("=.="); // aaa
solution("123_.def"); // 123_.def
solution("abcdefghijklmn.p"); // abcdefghijklmn

// https://programmers.co.kr/learn/courses/30/lessons/72410
