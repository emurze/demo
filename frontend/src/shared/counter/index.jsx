import React, { useEffect, useState } from "react"

const Counter = () => {
  const [count, setCount] = useState(0)
  const [color, setColor] = useState("green")

  useEffect(() => {
    const handleResize = () => {
      console.log("FUCK LERKA")
    }

    window.addEventListener("resize", handleResize)
    console.log("EVENT LISTENER ADDED")
    return () => {
      window.removeEventListener("resize", handleResize)
      console.log("EVENT LISTENER REMOVED")
    }
  }, [])

  useEffect(() => {
    document.title = `Count ${count}`
    console.log("DID MOUNT OR UPDATE")
    return () => {
      console.log("IT'S UNMOUNTED")
    }
  }, [count])

  useEffect(() => {
    console.log("COLOR DID MOUNT OR UPDATE")
  }, [color])

  const increment = () => setCount(count + 1)
  const subtract = () => setCount(count - 1)
  const setRedColor = () => setColor("red")
  const setGreenColor = () => setColor("green")

  return (
    <>
      <div className="counter">
        <div>Co unt: {count}</div>
        <button onClick={increment}>add</button>
        <button onClick={subtract}>Subtract</button>
      </div>
      <div>
        <div>Color {color}</div>
        <button onClick={setRedColor}>set red</button>
        <button onClick={setGreenColor}>set green</button>
      </div>
    </>
  )
}

export default Counter
