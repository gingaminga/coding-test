function solution(record) {
  const users = {}; // 유저 정보 저장

  record.forEach((message) => {
    const [action, id, nickname] = message.split(" ");

    if (action === "Leave") return;

    users[id] = {
      nickname,
    };
  });

  const answer = record
    .filter((message) => !message.startsWith("Change"))
    .map((message) => {
      const [action, id, nickname] = message.split(" ");

      let actionKo = "들어왔습니다.";
      if (action === "Leave") {
        actionKo = "나갔습니다.";
      }

      return `${users[id].nickname}님이 ${actionKo}`;
    });
  console.log(answer);

  return answer;
}

solution([
  "Enter uid1234 Muzi",
  "Enter uid4567 Prodo",
  "Leave uid1234",
  "Enter uid1234 Prodo",
  "Change uid4567 Ryan",
]);
// ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

// https://programmers.co.kr/learn/courses/30/lessons/42888
