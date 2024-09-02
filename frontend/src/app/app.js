import { BrowserRouter } from "react-router-dom"
import Layout from "../layout"
import Routes from "../pages/routes"
import "./styles/app.scss"
import { Provider } from "react-redux"
import { store } from "./store"

const App = () => {
  return (
    <div className="app">
      <BrowserRouter>
        <Provider store={store}>
          <Layout>
            <Routes />
          </Layout>
        </Provider>
      </BrowserRouter>
    </div>
  )
}

export default App
