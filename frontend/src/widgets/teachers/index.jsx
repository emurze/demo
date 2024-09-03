import React, { useEffect, useState } from "react"
import TeacherCard from "../../entities/teacher-card"
import "./styles.scss"
import { backendOrigin } from "../../app/constants"

const Teachers = () => {
  const [teachers, setTeachers] = useState([])
  const [isLoading, setIsLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    fetch(`${backendOrigin}/teachers/`)
      .then((resp) => {
        if (!resp.ok) {
          throw new Error("Network response was not ok")
        }
        return resp.json()
      })
      .then((json) => setTeachers(json))
      .catch((err) => {
        console.error("Failed to fetch teachers:", err)
        setError(err)
      })
      .finally(() => setIsLoading(false))
  }, [])

  console.log("Teachers", teachers)
  console.log(error)

  return (
    <section className="teachers">
      {isLoading && <p>Loading...</p>}
      {error && <p>{error}</p>}
      {!isLoading && !error && teachers.length === 0 && (
        <p>No teachers found.</p>
      )}
      {!isLoading &&
        !error &&
        teachers.length > 0 &&
        teachers.map((teacher) => (
          <TeacherCard
            key={teacher.id}
            id={teacher.id}
            name={teacher.title}
            description={teacher.description}
            difficulty={teacher.difficulty}
          />
        ))}
    </section>
  )
}

export default Teachers
