import React from 'react'
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import Home from './Home';

function router() {
    return (
        <div>
            <BrowserRouter>
            <Switch>
                

                <Route path='/test' component={() => <h1>This is test page</h1>}/>
            </Switch>
            
            </BrowserRouter>
            
        </div>
    )
}

export default router
