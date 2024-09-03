import React, { useState } from "react"
import "./styles.scss"
import SubjectCard from "../../entities/subject-card"

const Subjects = () => {
  const [subjects, setSubjects] = useState([])

  return (
    <div className="subjects">
      {subjects.map((subject, idx) => (
        <SubjectCard subject={subject} key={idx} />
      ))}
    </div>
  )
}

export default Subjects
