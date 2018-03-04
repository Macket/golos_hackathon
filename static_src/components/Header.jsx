import React from 'react';
import AppBar from 'material-ui/AppBar';
import FlatButton from 'material-ui/FlatButton';

function handleClick() {
    window.alert('onClick triggered on the title component');
}

const styles = {
    appBar: {
        backgroundColor: 'white',
    },
    title: {
        cursor: 'pointer',
        color: 'black',
    },
    icon: {
        cursor: 'pointer',
        color: 'black',
    },
};

/**
 * This example uses an [IconButton](/#/components/icon-button) on the left, has a clickable `title`
 * through the `onClick` property, and a [FlatButton](/#/components/flat-button) on the right.
 */
const Header = () => (
    <AppBar
        style={ styles.appBar }
        title={ <span style={ styles.title }>Title</span> }
        onTitleClick={ handleClick }
        iconElementLeft={ <img src="/static/logo.jpg" width="40" height="40" /> }
        iconElementRight={ <FlatButton style={ styles.icon } label="Save" /> }
    />
);

export default Header;
