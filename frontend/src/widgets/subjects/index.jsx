import React from "react"
import "./styles.scss"
import SubjectCard from "../../entities/subject-card"

const Subjects = () => {
  const subjects = [
    {
      id: 1,
      title: "философия",
      teachers: ["Шепетюк Виталий Васильевич", "Шкундич Алексей Олегович"],
    },
    {
      id: 2,
      title: "Линейная алгебра и геометрия",
      teachers: ["Филипович Оксана Фёдоровн", "Рачковский Николай Николаевич"],
    },
    {
      id: 3,
      title: "Кураторский,информационный час",
      teachers: ["Кудина Анна Вячеславовна"],
    },
    {
      id: 4,
      title: "Химия",
      teachers: ["Бычек Инга Владимировна"],
    },
    {
      id: 5,
      title: "Основы алгоритмизации и программирования",
      teachers: [
        "Кривоносова Татьяна Михайловна",
        "Панасик Алексей Александрович",
      ],
    },
    {
      id: 6,
      title: "Инженерная компьютерная графика",
      teachers: ["Столер Владимир Алексеевич"],
    },
    {
      id: 7,
      title: "Белорусский язык",
      teachers: ["Дапиро Татьяна Петровна"],
    },
  ]

  return (
    <div className="subjects">
      {subjects.map((subject, idx) => (
        <SubjectCard subject={subject} key={idx} />
      ))}
    </div>
  )
}

export default Subjects
