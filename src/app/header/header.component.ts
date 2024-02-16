import { Component } from '@angular/core';
import { MatTabGroup } from '@angular/material/tabs';
import { MatTab } from '@angular/material/tabs';
import { ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [MatTabGroup, MatTab],
  templateUrl: './header.component.html',
  styleUrl: './header.component.css',
  encapsulation: ViewEncapsulation.None
})
export class HeaderComponent {
  title: string = "Space and Rocketry Calculator (SpARC)";

  customLabelClass = 'mat-tab-label-custom';
}
