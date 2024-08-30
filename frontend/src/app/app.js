import { BrowserRouter } from "react-router-dom"
import Layout from "../layout"
import Routing from "../pages/routing"
import "./styles/app.scss"

const App = () => {
  return (
    <div className="app">
      <BrowserRouter>
        <Layout>
          <Routing />
        </Layout>
      </BrowserRouter>
    </div>
  )
}

export default App
