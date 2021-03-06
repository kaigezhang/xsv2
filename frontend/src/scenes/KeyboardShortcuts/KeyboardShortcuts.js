// @flow
import React from 'react';
import styled from 'styled-components';
import Key from 'components/Key';
import Flex from 'shared/components/Flex';
import HelpText from 'components/HelpText';

function KeyboardShortcuts() {
  return (
    <Flex column>
      <HelpText>
        Xueshu.io 旨在提供快熟方便的知识管理工具，你可以利用以下的快捷按键加快你的工作
        {"'"} 当然还有Markdown
      </HelpText>

      <h2>Navigation</h2>
      <List>
        <Keys>
          <Key>e</Key>
        </Keys>
        <Label>Edit current document</Label>

        <Keys>
          <Key>m</Key>
        </Keys>
        <Label>Move current document</Label>

        <Keys>
          <Key>/</Key> or <Key>t</Key>
        </Keys>
        <Label>Jump to search</Label>

        <Keys>
          <Key>d</Key>
        </Keys>
        <Label>Jump to dashboard</Label>

        <Keys>
          <Key>?</Key>
        </Keys>
        <Label>Open this guide</Label>
      </List>

      <h2>Editor</h2>
      <List>
        <Keys>
          <Key>⌘</Key> + <Key>Enter</Key>
        </Keys>
        <Label>Save and exit document edit mode</Label>
        <Keys>
          <Key>⌘</Key> + <Key>S</Key>
        </Keys>
        <Label>Save document and continue editing</Label>
        <Keys>
          <Key>⌘</Key> + <Key>Esc</Key>
        </Keys>
        <Label>Cancel editing</Label>

        <Keys>
          <Key>⌘</Key> + <Key>b</Key>
        </Keys>
        <Label>Bold</Label>
        <Keys>
          <Key>⌘</Key> + <Key>i</Key>
        </Keys>
        <Label>Italic</Label>
        <Keys>
          <Key>⌘</Key> + <Key>u</Key>
        </Keys>
        <Label>Underline</Label>
        <Keys>
          <Key>⌘</Key> + <Key>d</Key>
        </Keys>
        <Label>Strikethrough</Label>
        <Keys>
          <Key>⌘</Key> + <Key>k</Key>
        </Keys>
        <Label>Link</Label>
        <Keys>
          <Key>⌘</Key> + <Key>z</Key>
        </Keys>
        <Label>Undo</Label>
        <Keys>
          <Key>⌘</Key> + <Key>Shift</Key> + <Key>z</Key>
        </Keys>
        <Label>Redo</Label>
      </List>

      <h2>Markdown</h2>
      <List>
        <Keys>
          <Key>#</Key> <Key>Space</Key>
        </Keys>
        <Label>Large header</Label>
        <Keys>
          <Key>##</Key> <Key>Space</Key>
        </Keys>
        <Label>Medium header</Label>
        <Keys>
          <Key>###</Key> <Key>Space</Key>
        </Keys>
        <Label>Small header</Label>

        <Keys>
          <Key>1.</Key> <Key>Space</Key>
        </Keys>
        <Label>Numbered list</Label>
        <Keys>
          <Key>-</Key> <Key>Space</Key>
        </Keys>
        <Label>Bulleted list</Label>
        <Keys>
          <Key>[ ]</Key> <Key>Space</Key>
        </Keys>
        <Label>Todo list</Label>
        <Keys>
          <Key>&gt;</Key> <Key>Space</Key>
        </Keys>
        <Label>Blockquote</Label>
        <Keys>
          <Key>---</Key>
        </Keys>
        <Label>Horizontal divider</Label>
        <Keys>
          <Key>```</Key>
        </Keys>
        <Label>Code block</Label>

        <Keys>_italic_</Keys>
        <Label>Italic</Label>
        <Keys>**bold**</Keys>
        <Label>Bold</Label>
        <Keys>~~strikethrough~~</Keys>
        <Label>Strikethrough</Label>
        <Keys>`code`</Keys>
        <Label>Inline code</Label>
      </List>
    </Flex>
  );
}

const List = styled.dl`
  width: 100%;
  overflow: hidden;
  padding: 0;
  margin: 0;
`;

const Keys = styled.dt`
  float: left;
  width: 25%;
  padding: 0 0 4px;
  margin: 0;
`;

const Label = styled.dd`
  float: left;
  width: 75%;
  padding: 0 0 4px;
  margin: 0;
`;

export default KeyboardShortcuts;
