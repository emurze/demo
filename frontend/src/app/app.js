import { BrowserRouter } from "react-router-dom"
import Layout from "../layout"
import Routes from "../pages/routes"
import "./styles/app.scss"

const App = () => {
  return (
    <div className="app">
      {/*<Provider store={store}>*/}
      <BrowserRouter>
        <Layout>
          <Routes />
        </Layout>
      </BrowserRouter>
      {/*</Provider>*/}
    </div>
  )
}

export default App
